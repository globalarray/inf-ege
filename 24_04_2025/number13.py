from ipaddress import *

r = 0

for i in range(33):
    try:
        net = ip_network("84.23.84.0/" + str(i))

        if ip_address("84.23.84.23") in net:
            mask = list(map(int, str(net.netmask).split('.')))
            r = max(mask[3] + mask[2], r)
    except:
        _ = 1
print(r)
