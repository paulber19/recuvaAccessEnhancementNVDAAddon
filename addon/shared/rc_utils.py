#appModules\recuva\rc_utils.py
#A part of recuvaAccessEnhancement add-on
#Copyright (C) 2020, paulber19
#This file is covered by the GNU General Public License.


import addonHandler
addonHandler.initTranslation()
import wx
import api
import speech
import winUser

from logHandler import log
import os
import sys
_curAddon = addonHandler.getCodeAddon()
sharedPath = os.path.join(_curAddon.path, "shared")
sys.path.append(sharedPath)
from rc_py3Compatibility import longint
del sys.path[-1]

# winuser.h constant
SC_MAXIMIZE     = 0xF030
WS_MAXIMIZE         = 0x01000000
WM_SYSCOMMAND = 0x112
# window style
WS_MAXIMIZE = longint(0x01000000) #The window is initially maximized
WS_MAXIMIZEBOX = longint(0x00010000) #The window has a maximize button. Cannot be combined with the WS_EX_CONTEXTHELP style. The WS_SYSMENU style must also be specif 
WS_MINIMIZE = longint(0x20000000) # The window is initially minimized. Same as the WS_ICONIC style.
WS_MINIMIZEBOX= longint(0x00020000) #The window has a minimize button. Cannot be combined with the WS_EX_CONTEXTHELP style. The WS_SYSMENU style must also be specif
def isMaximized(hWnd):
	windowStyle = winUser.getWindowStyle(hWnd)
	return (windowStyle & WS_MAXIMIZE) 
def maximizeWindow(hWnd):
	windowStyle = winUser.getWindowStyle(hWnd)
	maximized = windowStyle & WS_MAXIMIZE
	if not maximized and windowStyle & WS_MAXIMIZEBOX :
		try:
			winUser.PostMessage (hWnd, WM_SYSCOMMAND, SC_MAXIMIZE,0)
		except:
			pass

