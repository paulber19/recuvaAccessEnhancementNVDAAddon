# -*- coding: UTF-8 -*-
import os.path

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.


# Full getext (please don't change)
def _(arg):
	return arg


# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines
	# at: https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name": "recuvaAccessEnhancement",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation
	# and add-on information.
	"addon_summary": _("Recuva file recovery: accessibility enhancement"),
	# Add-on description
	# Translators: Long description to be shown for this add-on
	# on add-on information from add-ons manager
	"addon_description": _("""Although this application is relatively well accessible, this extension attempts to improve the accessibility of the Recuva file recovery software by:

* naming certain unlabeled objects,
* preventing unnecessary focus from being placed on unknown objects,
* adding the script "KEY_Search_RESULT" to re-read the overall result of the search,
* automatically maximizing the window displaying the search result.
"""),

	# version
	"addon_version": "1.2",
	# Author(s)
	"addon_author": "paulber19",
	# URL for the add-on documentation support
	"addon_url": "paulber19@laposte.net",
	# Documentation file name
	"addon_docFileName": "addonUserManual.html",
	# Minimum NVDA version supported (e.g. "2018.3")
	"addon_minimumNVDAVersion": "2019.1",
	# Last NVDA version supported/tested
	# (e.g. "2018.4", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion": "2020.4",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel": None,
}


# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [
	os.path.join("addon", "*.py"),
	os.path.join("addon", "shared", "*.py"),
	os.path.join("addon", "appModules", "recuva", "*.py"),
	os.path.join("addon", "globalPlugins", "recuvaAccessEnhancement", "*.py"),
	os.path.join(
		"addon",
		"globalPlugins", "recuvaAccessEnhancement", "updateHandler", "*.py"),
	]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory,
# not to the root directory of your addon sources.
excludedFiles = []

# Base language for the NVDA add-on
# If your add-on is written in a language other than english, modify this variable.
# For example, set baseLanguage to "es" if your add-on is primarily written in spanish.
baseLanguage = "en"