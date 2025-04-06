from ipaddress import ip_network, ip_address

cnt = 0

net = ip_network("195.102.65.64/255.255.255.192", False)

for ip in net:
    b = str(ip).split('.')

    s = bin(int(b[3]))[2:]

    if len(s) < 8:
        s = ('0' * (8 - len(s))) + s

    if s.count('1') == s.count('0'):
        cnt += 1
print(cnt)
