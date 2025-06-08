from ipaddress import ip_network

net = ip_network("172.16.192.0/255.255.192.0", False)

cnt = 0

for ip in net:
    if int(str(ip).split('.')[-1]) % 2 != 0 and f'{ip:b}'.count('1') % 3 == 0:
        cnt += 1
print(cnt)
