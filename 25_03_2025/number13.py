from ipaddress import ip_network

net = ip_network("105.224.200.224/255.255.255.224")

cnt = 0

for ip in net.hosts():
    if (bin(int("".join(str(ip).split('.'))))[2:]).count('1') % 4 == 0:
        cnt += 1
print(cnt)
