from ipaddress import ip_network

def to_byte(v):
    return ("0" * (8 -  len(v))) + v

mask = "".join(map(lambda x: to_byte(bin(int(x))[2:]), "0.0.7.255".split('.'))).replace("0", "*", -1).replace("1", "0", -1).replace("*", "1", -1)

net = ip_network("172.16.80.0/" + str(mask.count('1')), False)

cnt = 0

for ip in net:
    if "".join(map(lambda x: bin(int(x))[2:], str(ip).split('.'))).count('1') % 3 != 0:
        cnt += 1
print(cnt)
