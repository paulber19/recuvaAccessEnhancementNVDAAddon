# shared\rc_utils.py
# A part of recuvaAccessEnhancement add-on
# Copyright (C) 2020-2024 paulber19
# This file is covered by the GNU General Public License.


import addonHandler
import winUser
import speech.speech
try:
	# NVDA >= 2024.1
	speakOnDemand = speech.speech.SpeechMode.onDemand
except AttributeError:
	# NVDA <= 2023.3
	speakOnDemand = None

addonHandler.initTranslation()
# winuser.h constant
SC_MAXIMIZE = 0xF030
WS_MAXIMIZE = 0x01000000
WM_SYSCOMMAND = 0x112
# window style
# The window is initially maximized
WS_MAXIMIZE = 0x01000000
# The window has a maximize button.
# Cannot be combined with the WS_EX_CONTEXTHELP style.
# The WS_SYSMENU style must also be specif
WS_MAXIMIZEBOX = 0x00010000
# The window is initially minimized.
# Same as the WS_ICONIC style.
WS_MINIMIZE = 0x20000000
# The window has a minimize button.
# Cannot be combined with the WS_EX_CONTEXTHELP style.
# The WS_SYSMENU style must also be specif
WS_MINIMIZEBOX = 0x00020000


def isMaximized(hWnd):
	windowStyle = winUser.getWindowStyle(hWnd)
	return (windowStyle & WS_MAXIMIZE)


def maximizeWindow(hWnd):
	windowStyle = winUser.getWindowStyle(hWnd)
	maximized = windowStyle & WS_MAXIMIZE
	if not maximized and windowStyle & WS_MAXIMIZEBOX:
		try:
			winUser.PostMessage(hWnd, WM_SYSCOMMAND, SC_MAXIMIZE, 0)
		except Exception:
			pass


def executeWithSpeakOnDemand(func , *args, **kwargs):
	from speech.speech import _speechState, SpeechMode
	if not speakOnDemand or _speechState.speechMode != SpeechMode.onDemand:
		return func( *args, **kwargs)
	_speechState.speechMode  = SpeechMode.talk
	ret = func(*args, **kwargs)
	_speechState.speechMode = SpeechMode.onDemand
	return ret


def messageWithSpeakOnDemand(msg):
	executeWithSpeakOnDemand(ui.message, msg)
