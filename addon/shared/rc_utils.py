# shared\rc_utils.py
# A part of recuvaAccessEnhancement add-on
# Copyright (C) 2020, paulber19
# This file is covered by the GNU General Public License.


import addonHandler
import winUser

from rc_py3Compatibility import longint  # noqa:E402
_curAddon = addonHandler.getCodeAddon()

addonHandler.initTranslation()
# winuser.h constant
SC_MAXIMIZE = 0xF030
WS_MAXIMIZE = 0x01000000
WM_SYSCOMMAND = 0x112
# window style
# The window is initially maximized
WS_MAXIMIZE = longint(0x01000000)
# The window has a maximize button.
# Cannot be combined with the WS_EX_CONTEXTHELP style.
# The WS_SYSMENU style must also be specif
WS_MAXIMIZEBOX = longint(0x00010000)
# The window is initially minimized.
# Same as the WS_ICONIC style.
WS_MINIMIZE = longint(0x20000000)
# The window has a minimize button.
# Cannot be combined with the WS_EX_CONTEXTHELP style.
# The WS_SYSMENU style must also be specif
WS_MINIMIZEBOX = longint(0x00020000)


def isMaximized(hWnd):
	windowStyle = winUser.getWindowStyle(hWnd)
	return (windowStyle & WS_MAXIMIZE)


def maximizeWindow(hWnd):
	windowStyle = winUser.getWindowStyle(hWnd)
	maximized = windowStyle & WS_MAXIMIZE
	if not maximized and windowStyle & WS_MAXIMIZEBOX:
		try:
			winUser.PostMessage(hWnd, WM_SYSCOMMAND, SC_MAXIMIZE, 0)
		except:  # noqa:E722
			pass
