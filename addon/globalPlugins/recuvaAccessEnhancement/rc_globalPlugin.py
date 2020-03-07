#globalPlugins\recuvaAccessEnhancement\rc_globalPlugin.py
# a part of recuvaAccessEnhancement add-on
#Copyright (C) 2020 Paulber19
#This file is covered by the GNU General Public License.


import addonHandler
addonHandler.initTranslation()
import globalPluginHandler
from logHandler import log,_getDefaultLogFilePath
import gui
import wx
import os
import globalVars
import sys
addon = addonHandler.getCodeAddon()
path = os.path.join(addon.path, "shared")
sys.path.append(path)
from  rc_addonConfigManager import _addonConfigManager
del sys.path[-1]

class RecuvaGlobalPlugin(globalPluginHandler.GlobalPlugin):
	
	def __init__(self, *args, **kwargs):
		super(RecuvaGlobalPlugin, self).__init__(*args, **kwargs)
		self.installSettingsMenu()
		from . updateHandler import autoUpdateCheck
		if _addonConfigManager.toggleAutoUpdateCheck(False):
			autoUpdateCheck(releaseToDev = _addonConfigManager.toggleUpdateReleaseVersionsToDevVersions     (False))
	def installSettingsMenu(self):
		self.preferencesMenu= gui.mainFrame.sysTrayIcon.preferencesMenu
		from .rc_configGui import RecuvaSettingsDialog
		self.menu = self.preferencesMenu.Append(wx.ID_ANY,
			RecuvaSettingsDialog.title + " ...",
			"")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onMenu, self.menu)
	
	def deleteSettingsMenu(self):
		try:
			self.preferencesMenu.Remove (self.menu )
		except:
			pass
	
	def onMenu(self, evt):
		from .rc_configGui import RecuvaSettingsDialog
		gui.mainFrame._popupSettingsDialog(RecuvaSettingsDialog)

	def terminate(self):
		self.deleteSettingsMenu()
		super(RecuvaGlobalPlugin, self).terminate()
	
	

