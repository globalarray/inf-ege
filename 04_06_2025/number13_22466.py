from ipaddress import ip_network

net = ip_network("98.71.254.171/255.248.0.0", False)

for ip in net.hosts():
    if f'{ip:b}'.count('1') % 7 == 0:
        print("".join(str(ip).split('.')))
        break
