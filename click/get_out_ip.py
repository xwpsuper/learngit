#同步查询外网ip

import urllib.request
from json import load
import time

def get_out_ip():

    while True:
        try:
            ip0 = urllib.request.urlopen('http://ip.42.pl/raw', timeout=1).read().decode('utf-8')
            if ip0:
                print('http://ip.42.pl/raw:', ip0)
                return ip0
                break
        except:
            pass
        try:
            ip1 = load(urllib.request.urlopen('http://jsonip.com', timeout=1))['ip']  
            if ip1:
                print('http://jsonip.com:', ip1)
                return ip1
                break
        except:
            pass

        try:
            ip2 = load(urllib.request.urlopen('http://httpbin.org/ip', timeout=1))['origin']  
            if ip2:
                print('http://httpbin.org/ip:', ip2)
                return ip2
                break
        except:
            pass

        try:
            ip3 = load(urllib.request.urlopen('https://api.ipify.org/?format=json', timeout=0.5))['ip']  
            if ip3:
                print('https://api.ipify.org/?format=json:', ip3)
                return ip3
                break
        except:
            pass

        time.sleep(1)

while True:
    j = get_out_ip()
    if j != 0:
        break
    else:
        time.sleep(1)
print(j,1)