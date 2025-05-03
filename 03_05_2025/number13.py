from ipaddress import *

for x in range(256):
    try:
        net = ip_network("172.16.168.0/255.255.255." + str(x), False)

        cnt = 0

        for ip in net:
            if f'{ip:b}'.count('0') % 7 == 0:
                cnt += 1
            if cnt > 35:
                break
        if cnt == 35:
            print(x)
    except:
        _ = 1
