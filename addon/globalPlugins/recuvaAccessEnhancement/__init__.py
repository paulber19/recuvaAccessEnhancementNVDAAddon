# globalPlugins\recuvaAccessEnhancement\__init__.py
# a part of recuvaAccessEnhancement add-on
# Copyright (C) 2020 Paulber19
# This file is covered by the GNU General Public License.

import globalVars
import config

# this add-on is disabled when loading in the secure screen,
# as well as if NVDA is running as a Windows Store Desktop Bridge application.
if globalVars.appArgs.secure\
	or (hasattr(config, "isAppX") and config.isAppX):
	import globalPluginHandler

	class GlobalPlugin (globalPluginHandler.GlobalPlugin):
		pass
else:
	from . import rc_globalPlugin

	class GlobalPlugin (rc_globalPlugin.RecuvaGlobalPlugin):
		pass
