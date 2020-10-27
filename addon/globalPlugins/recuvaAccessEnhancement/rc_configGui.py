# globalPlugins\recuvaAccessEnhancement\rc_configGui.py
# a part of recuvaAccessEnhancement add-on
# Copyright 2020,paulber19
# released under GPL.

import addonHandler
import os
import wx
import gui
from gui.settingsDialogs import SettingsDialog
import sys
_curAddon = addonHandler.getCodeAddon()
path = os.path.join(_curAddon.path, "shared")
sys.path.append(path)
from rc_addonConfigManager import _addonConfigManager  # noqa:E402
del sys.path[-1]

addonHandler.initTranslation()
_addonSummary = _curAddon.manifest['summary']


class RecuvaSettingsDialog(SettingsDialog):
	# Translators: This is the label for the Recuva settings dialog.
	title = _("%s add-on - settings") % _addonSummary

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: This is the label for a group of editing options
		# in the Recuva settings panel.
		groupText = _("Update")
		group = gui.guiHelper.BoxSizerHelper(
			self,
			sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=groupText), wx.VERTICAL))
		sHelper.addItem(group)
		# Translators: This is the label for a checkbox in the Recuva SettingsDialog.
		labelText = _("Automatically check for &updates ")
		self.autoCheckForUpdatesCheckBox = group.addItem(
			wx.CheckBox(self, wx.ID_ANY, label=labelText))
		self.autoCheckForUpdatesCheckBox.SetValue(
			_addonConfigManager.toggleAutoUpdateCheck(False))
		# Translators: This is the label for a checkbox in the Recuva settings panel.
		labelText = _("Update also release versions to &developpement versions")
		self.updateReleaseVersionsToDevVersionsCheckBox = group.addItem(
			wx.CheckBox(self, wx.ID_ANY, label=labelText))
		self.updateReleaseVersionsToDevVersionsCheckBox.SetValue(
			_addonConfigManager.toggleUpdateReleaseVersionsToDevVersions(False))
		# translators: label for a button in recuva settings panel.
		labelText = _("&Check for update")
		checkForUpdateButton = wx.Button(self, label=labelText)
		group.addItem(checkForUpdateButton)
		checkForUpdateButton.Bind(wx.EVT_BUTTON, self.onCheckForUpdate)

	def onCheckForUpdate(self, evt):
		from .updateHandler import addonUpdateCheck
		wx.CallAfter(
			addonUpdateCheck, auto=False,
			releaseToDev=_addonConfigManager.toggleUpdateReleaseVersionsToDevVersions(False))  # noqa:E501
		self.Close()

	def postInit(self):
		pass

	def saveSettingChanges(self):
		if self.autoCheckForUpdatesCheckBox.IsChecked() != _addonConfigManager .toggleAutoUpdateCheck(False):  # noqa:E501
			_addonConfigManager .toggleAutoUpdateCheck(True)
		if self.updateReleaseVersionsToDevVersionsCheckBox.IsChecked() != _addonConfigManager .toggleUpdateReleaseVersionsToDevVersions(False):  # noqa:E501
			_addonConfigManager .toggleUpdateReleaseVersionsToDevVersions(True)

	def onOk(self, evt):
		self.saveSettingChanges()
		super(RecuvaSettingsDialog, self).onOk(evt)
