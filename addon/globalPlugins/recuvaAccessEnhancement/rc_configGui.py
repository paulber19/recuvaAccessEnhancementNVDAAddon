# globalPlugins\recuvaAccessEnhancement\rc_configGui.py
# a part of recuvaAccessEnhancement add-on
# Copyright 2020-2022 paulber19
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
from rc_addonConfigManager import _addonConfigManager
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
		labelText = _("Automatically check for &updates")
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
		# translators: this is a label for a button in update settings panel.
		labelText = _("View &history")
		seeHistoryButton = wx.Button(self, label=labelText)
		sHelper.addItem(seeHistoryButton)
		seeHistoryButton.Bind(wx.EVT_BUTTON, self.onSeeHistory)

	def onCheckForUpdate(self, evt):
		from .updateHandler import addonUpdateCheck
		self.saveSettingChanges()
		releaseToDevVersion = self.updateReleaseVersionsToDevVersionsCheckBox.IsChecked()
		wx.CallAfter(addonUpdateCheck, auto=False, releaseToDev=releaseToDevVersion)
		self.Close()

	def onSeeHistory(self, evt):
		addon = addonHandler.getCodeAddon()
		from languageHandler import getLanguage
		curLang = getLanguage()
		theFile = os.path.join(addon.path, "doc", curLang, "changes.html")
		if not os.path.exists(theFile):
			lang = curLang.split("_")[0]
			theFile = os.path.join(addon.path, "doc", lang, "changes.html")
			if not os.path.exists(theFile):
				lang = "en"
				theFile = os.path.join(addon.path, "doc", lang, "changes.html")
		os.startfile(theFile)

	def postInit(self):
		self.autoCheckForUpdatesCheckBox.SetFocus()

	def saveSettingChanges(self):
		if self.autoCheckForUpdatesCheckBox.IsChecked() != _addonConfigManager .toggleAutoUpdateCheck(False):
			_addonConfigManager .toggleAutoUpdateCheck(True)
		if self.updateReleaseVersionsToDevVersionsCheckBox.IsChecked() != (
			_addonConfigManager .toggleUpdateReleaseVersionsToDevVersions(False)):
			_addonConfigManager .toggleUpdateReleaseVersionsToDevVersions(True)

	def onOk(self, evt):
		self.saveSettingChanges()
		super(RecuvaSettingsDialog, self).onOk(evt)
