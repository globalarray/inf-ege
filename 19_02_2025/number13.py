from ipaddress import ip_network

net = ip_network("192.168.0.1/255.255.254.0", False)

print(len(list(net.hosts())))
