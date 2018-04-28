import win32gui
import win32api
import win32con
import time

time.sleep(3)
win32api.keybd_event(121, 85, 0, 0)
win32api.keybd_event(121, 85, win32con.KEYEVENTF_KEYUP, 0)