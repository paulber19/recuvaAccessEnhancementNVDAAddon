# appModules\recuva\__init__.py
# a part of recuvaAccessEnhancement add-on
# Copyright (C) 2020-2021 Paulber19
# This file is covered by the GNU General Public License.
# Released under GPL 2

import addonHandler
import appModuleHandler
import controlTypes
import os
import ui
import api
import NVDAObjects
from NVDAObjects.IAccessible import IAccessible
import sys
_curAddon = addonHandler.getCodeAddon()
sharedPath = os.path.join(_curAddon.path, "shared")
sys.path.append(sharedPath)
from rc_utils import maximizeWindow  # noqa:E402
del sys.path[-1]

addonHandler.initTranslation()
_addonSummary = _curAddon.manifest['summary']
_addonVersion = _curAddon.manifest['version']
_scriptCategory = str(_addonSummary)
_typeRadioButtonControlIDs = [1048, 1049, 1050, 1051, 1061, 1062, 1109]


class Button(NVDAObjects.NVDAObject):
	def _get_name(self):
		name = super(Button, self)._get_name()
		name = name.replace(" >", "")
		name = name.replace("< ", "")
		return name


class TypeRadioButton(NVDAObjects.NVDAObject):
	role = controlTypes.ROLE_LISTITEM

	def _get_name(self):
		name = super(TypeRadioButton, self)._get_name()
		return name.replace("&", "")

	def _get_states(self):
		states = super(TypeRadioButton, self)._get_states()
		states.discard(controlTypes.STATE_CHECKED)
		return states


class TypePropertyPage(NVDAObjects.NVDAObject):
	role = controlTypes.ROLE_LIST

	def _get_name(self):
		if self.childCount == 14:
			name = _("File' type to retrive:")
		elif self.childCount == 17:
			name = _("Where to search:")
		else:
			name = super(TypePropertyPage, self)._get_name()
		return name

	def event_focusEntered(self):
		self.description = ""
		super(TypePropertyPage, self).event_focusEntered()


class FakeStaticText(NVDAObjects.NVDAObject):
	def _get_name(self):
		return ""


class MainPropertyPage(NVDAObjects.NVDAObject):
	def _get_description(self):
		return ""


class ResultList(IAccessible):
	def _get_name(self):
		return _("Search's result:")

	def event_gainFocus(self):
		super(ResultList, self).event_gainFocus()
		maximizeWindow(self.windowHandle)


class FakeStaticWindow(NVDAObjects.NVDAObject):
	def _get_name(self):
		return ""

	def event_gainFocus(self):
		# obtain focus unusely, so set focus on property page
		parent = self.parent.parent
		parent.firstChild.setFocus()


class UpdateSearchButton(IAccessible):
	pass


class SearchLocationComboBox(IAccessible):
	def initOverlayClass(self):
		self.bindGesture("kb:shift+tab", "moveToUpdateSearchButton")

	def _get_name(self):
		return _("Search's location:")

	def script_moveToUpdateSearchButton(self, gesture):

		foreground = api.getForegroundObject()

		o = foreground.firstChild.next.next
		o.setFocus()


class FileTypeComboBox(IAccessible):
	def _get_name(self):
		return _("File's type:")


class AppModule(appModuleHandler.AppModule):
	scriptCategory = _scriptCategory

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)

	def terminate(self):
		super(AppModule, self).terminate()

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == controlTypes.ROLE_RADIOBUTTON\
			and obj.windowControlID in _typeRadioButtonControlIDs:
			clsList.insert(0, TypeRadioButton)
			return
		if obj.role == controlTypes.ROLE_BUTTON:
			clsList.insert(0, Button)
			return
		if obj.role == controlTypes.ROLE_PROPERTYPAGE and obj.childCount in [14, 17]:
			# file type and search localization property page
			clsList.insert(0, TypePropertyPage)
			return
		if obj.role == controlTypes.ROLE_PROPERTYPAGE\
			and obj.windowControlID == 1045:
			clsList.insert(0, MainPropertyPage)
			return
		if obj.role == controlTypes.ROLE_STATICTEXT:
			if obj.windowControlID == 1038:
				clsList.insert(0, FakeStaticText)
				return
			if obj.windowControlID == 1020:
				# search result text
				self.searchResultObject = obj

		if obj.role == controlTypes.ROLE_LIST\
			and obj.windowClassName == "RC Files list"\
			or obj.role == controlTypes.ROLE_TREEVIEW\
			and obj.windowClassName == "RC Files Tree":
			clsList.insert(0, ResultList)
			return
		if obj.windowClassName == "Static" and obj.windowControlID == 1022:
			clsList.insert(0, FakeStaticWindow)
			return
		if obj.windowClassName == "ATL:009E5808" and obj.windowControlID == 1026:
			# update search button
			clsList.insert(0, UpdateSearchButton)
			return
		if obj.windowClassName == "ComboBox":
			if obj.windowControlID == 1013:
				# advanced search location combo box
				clsList.insert(0, SearchLocationComboBox)
				return
			if obj.windowControlID == 1006:
				clsList.insert(0, FileTypeComboBox)
				return

	def event_NVDAObject_init(self, obj):
		pass

	def event_appModule_gainFocus(self):
		pass

	def event_appModule_loseFocus(self):
		pass

	def event_gainFocus(self, obj, nextHandler):
		nextHandler()

	def event_focusEntered(self, obj, nextHandler):
		nextHandler()

	def script_reportSearchResult(self, gesture):
		if hasattr(self, "searchResultObject"):
			ui.message(self.searchResultObject.name)

	script_reportSearchResult.__doc__ = _("Report the result of the search")

	def script_test(self, gesture):
		ui.message("test")

	__gestures = {
		"kb:alt+control+r": "reportSearchResult",
		"kb:alt+control+f10": "test",
		}
