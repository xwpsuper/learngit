from __future__ import print_function

import win32gui
import win32api
import win32con
import time
import ctypes, sys
import json
import requests
import urllib.request
from json import load



def main_():
    #查找句柄
    def find_hwnd(hclass, htitle):
        return win32gui.FindWindow(hclass, htitle)
    
    #查找子句柄
    def get_hwnd_child(fhwnd, hwndChildList = []):
        win32gui.EnumChildWindows(fhwnd, lambda hwnd, param: param.append(hwnd), hwndChildList)
        return hwndChildList
    
    #牛魔点击按键函数
    def nmclick(hwnd):
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        x = left + (right - left) / 3
        y = top + (bottom - top) * 0.8
        win32api.SetCursorPos([int(x), int(y)])  # 为鼠标焦点设定一个位置
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        time.sleep(0.1)
    
    #把激活句柄
    def hactive(hwnd):
        win32gui.SetActiveWindow(hwnd)
        win32gui.SetForegroundWindow(hwnd)
    
    #通过牛逼更换硬件信息
    def change_nb_things(hwnd):

        hactive(hwnd)
        for chwnd in get_hwnd_child(hwnd):
            if win32gui.GetWindowText(chwnd) == '一键修改':
                hwnd_buttom_fix = chwnd

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
    
    #点击一次牛魔按钮
    def one_nm_click(hwnd):
        try:
            hactive(hwnd)
        except:
            pass
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        time.sleep(0.5)
        nmclick(hwnd)
        time.sleep(5)
    
    #确认管理员身份运行
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    #查询外网ip
    def get_out_ip():
        count = 0
        while True:
            if count<=5:
                try:
                    ip0 = urllib.request.urlopen('http://ip.42.pl/raw', timeout=1).read().decode('utf-8')
                    if ip0:
                        print('http://ip.42.pl/raw:', ip0)
                        return ip0
                        break
                except:
                    pass

                try:
                    ip1 = json.load(urllib.request.urlopen('http://jsonip.com', timeout=1))['ip']  
                    if ip1:
                        print('http://jsonip.com:', ip1)
                        return ip1
                        break
                except:
                    pass

                try:
                    ip2 = json.load(urllib.request.urlopen('http://httpbin.org/ip', timeout=1))['origin']  
                    if ip2:
                        print('http://httpbin.org/ip:', ip2)
                        return ip2
                        break
                except:
                    pass

                try:
                    ip3 = json.load(urllib.request.urlopen('https://api.ipify.org/?format=json', timeout=0.5))['ip']  
                    if ip3:
                        print('https://api.ipify.org/?format=json:', ip3)
                        return ip3
                        break
                except:
                    pass

            else:
                print('网络：无Internet访问')
                return 'timeout'
                break

            count += 1
            time.sleep(0.5)
    
    #激活按键精灵句柄，模拟键盘点击F10（开始）或F12（停止）脚本
    def ajjl_f10orf12(hwnd, F):
        hactive(hwnd)
        print(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32api.keybd_event(F, 0, 0, 0)
        win32api.keybd_event(F, 0, win32con.KEYEVENTF_KEYUP, 0)


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
    ajjl_f10orf12(hwnd_ajjl, 123)

    if is_admin():
        #点击牛魔按钮
        one_nm_click(hwnd_nm)
		
        k = 0
        j = 0

        while True:

            j = get_out_ip()
            if j == 'timeout':
                change_nb_things(hwnd_nb)
            elif j != 0:
                break
            else:
                time.sleep(0.5)
				
        print(j)
        time.sleep(0.5)
     #   win32gui.ShowWindow(hwnd_nm, win32con.SW_SHOWMINIMIZED)
        print('first check')
        time.sleep(1)

        #发送请求确定切换things成功
        change_nb_things(hwnd_nb)
        print('change thing over')

        #再次点击牛魔按钮
        one_nm_click(hwnd_nm)
		
        #确认IP切换成功，不成功再次点击按钮
        while True:

            k = get_out_ip()
            if k == 'timeout':
                one_nm_click(hwnd_nm)
                change_nb_things(hwnd_nb)
                one_nm_click(hwnd_nm)

            elif k != j and k != 0:
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
        ajjl_f10orf12(hwnd_ajjl, 121)

        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

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
