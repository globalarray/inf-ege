from ipaddress import *

cnt = 0

for i in range(32, 0, -1):
    net = ip_network("206.123.209.193/" + str(i), False)

    if ip_address("206.123.210.118") in net:
        for ip in net:
            if bin(int(ip))[2:].count('1') == 15:
                cnt += 1
        break
print(cnt)
