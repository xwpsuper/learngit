from __future__ import print_function

import win32gui
import win32api
import win32con
import time
import ctypes, sys
import json
import requests

def main_():
    def find_hwnd(hclass, htitle):
        return win32gui.FindWindow(hclass, htitle)

    def get_hwnd_child(fhwnd, hwndChildList = []):
        win32gui.EnumChildWindows(fhwnd, lambda hwnd, param: param.append(hwnd), hwndChildList)
        return hwndChildList

    def nmclick(hwnd):
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        x = left + (right - left) / 3
        y = top + (bottom - top) * 0.8
        win32api.SetCursorPos([int(x), int(y)])  # 为鼠标焦点设定一个位置
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.1)

    def hactive(hwnd):
        win32gui.SetActiveWindow(hwnd)
        win32gui.SetForegroundWindow(hwnd)


    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def get_out_ip():
        url = r'http://2017.ip138.com/ic.asp'
        r = requests.get(url)
        txt = r.text
        ip = txt[txt.find("[") + 1: txt.find("]")]
        print('ip:' + ip)
        return ip


    hwnd_nb = find_hwnd("#32770", "牛B硬件信息修改大师")
    hwnd_nm = find_hwnd("Qt5QWindowIcon", "MainWindow")
    hwnd_ajjl = find_hwnd(None, "按键精灵")

    while True:
        if win32gui.FindWindow('MozillaWindowClass', None) == 0:
            time.sleep(2)
            break
        else:
            time.sleep(0.5)

    #控制按键精灵停止所有脚本 F12
    hactive(hwnd_ajjl)
    win32gui.ShowWindow(hwnd_ajjl, win32con.SW_RESTORE)
    win32api.keybd_event(123, 0, 0, 0)
    win32api.keybd_event(123, 0, win32con.KEYEVENTF_KEYUP, 0)

    if is_admin():
        #点击牛魔按钮
        hactive(hwnd_nm)
        win32gui.ShowWindow(hwnd_nm, win32con.SW_RESTORE)
        time.sleep(0.5)
        nmclick(hwnd_nm)
		
        k = 0
        j = 0

        while True:
            try:
                j = get_out_ip()
            except:
                pass
            if j != 0:
                break
            else:
                time.sleep(0.5)
				
        print(j)
        time.sleep(0.5)
     #   win32gui.ShowWindow(hwnd_nm, win32con.SW_SHOWMINIMIZED)
        print('first check')
        time.sleep(1)

        #发送请求确定切换things成功
        hactive(hwnd_nb)

        for hwnd in get_hwnd_child(hwnd_nb):
            if win32gui.GetWindowText(hwnd) == '一键修改':
                hwnd_buttom_fix = hwnd

        win32gui.PostMessage(hwnd_buttom_fix, win32con.BM_CLICK, 0, 0)

        timeout = 10
        st = time.time()

        while time.time() - st < timeout:
            mhwnd = win32gui.FindWindow("#32770", "Information")
            if mhwnd:
                break
            else:
                time.sleep(0.3)

        for handle_qd in get_hwnd_child(mhwnd):
            if win32gui.GetWindowText(handle_qd) == '确定':
                handle_qdqd = handle_qd
                win32gui.PostMessage(handle_qdqd, win32con.BM_CLICK, 0, 0)
                time.sleep(0.5)
        time.sleep(1)
        print('change thing over')

        #再次点击牛魔按钮
        hactive(hwnd_nm)
        win32gui.ShowWindow(hwnd_nm, win32con.SW_RESTORE)
        time.sleep(0.5)
        nmclick(hwnd_nm)
        time.sleep(5)
		
        #确认IP切换成功，不成功再次点击按钮
        while True:
            try:
                k = get_out_ip()
            except:
                pass
            if k != j and k != 0:
                break
            else:
                nmclick(hwnd_nm)
                time.sleep(1)
                nmclick(hwnd_nm)
                time.sleep(10)
        print(k)

        time.sleep(0.5)

    #    win32gui.ShowWindow(hwnd_nm, win32con.SW_SHOWMINIMIZED)
        print('change IP over')
        time.sleep(5)

        #启动按键精灵的F10开始脚本
        hactive(hwnd_ajjl)
        print(hwnd_ajjl)
        win32gui.ShowWindow(hwnd_ajjl, win32con.SW_RESTORE)
        win32api.keybd_event(121, 0, 0, 0)
        print(5)
        time.sleep(10)

    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:#in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

while True:
    main_()
    time.sleep(1)
# hwnd_root3 = win32gui.FindWindow("Qt5QWindowIcon", "MainWindow")
# print(hwnd_root3)
# win32gui.SetActiveWindow(hwnd_root3)
# win32gui.SetForegroundWindow(hwnd_root3)
# left, top, right, bottom = win32gui.GetWindowRect(hwnd_root3)
# print(left, top, right, bottom)
# x = left+(right-left)/3
# y = top+(bottom-top)*0.8
# win32api.SetCursorPos([int(x), int(y)])    #为鼠标焦点设定一个位置
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
# time.sleep(0.02)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
# time.sleep(0.5)
#
#
# hwnd_root = win32gui.FindWindow("#32770", "牛B硬件信息修改大师")
# win32gui.SetActiveWindow(hwnd_root)
# win32gui.SetForegroundWindow(hwnd_root)
# hwndChildList = []
# win32gui.EnumChildWindows(hwnd_root, lambda hwnd, param: param.append(hwnd), hwndChildList)
# for hwnd in hwndChildList:
#     if win32gui.GetWindowText(hwnd) == '一键修改':
#         hwnd_buttom_fix = hwnd
#         print(hwnd_buttom_fix, '一键修改')
# win32gui.PostMessage(hwnd_buttom_fix, win32con.BM_CLICK, 0, 0)
#
#
# timeout = 10
# st = time.time()
# while time.time() - st < timeout:
#     hwnd = win32gui.FindWindow("#32770", "Information")
#     if hwnd:
#         break
#     else:
#         time.sleep(0.3)
# print(hwnd)
#
#
# hwndChildList = []
# win32gui.EnumChildWindows(hwnd, lambda hwnd, param: param.append(hwnd), hwndChildList)
# for handle_qd in hwndChildList:
#     if win32gui.GetWindowText(handle_qd) == '确定':
#         handle_qdqd = handle_qd
#         print(handle_qd, '确定')
# win32gui.PostMessage(handle_qdqd, win32con.BM_CLICK, 0, 0)
# print(111)
#
#
# hwnd_root2 = win32gui.FindWindow("Qt5QWindowIcon", "MainWindow")
# print(hwnd_root2)
# win32gui.SetActiveWindow(hwnd_root2)
# win32gui.SetForegroundWindow(hwnd_root2)
# left, top, right, bottom = win32gui.GetWindowRect(hwnd_root2)
# print(left, top, right, bottom)
# x = left+(right-left)/3
# y = top+(bottom-top)*0.8
# win32api.SetCursorPos([int(x), int(y)])    #为鼠标焦点设定一个位置
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
# time.sleep(0.02)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
# time.sleep(0.1)
# print(222)
