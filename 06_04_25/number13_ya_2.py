from ipaddress import ip_network, ip_address

minByte = 256

for mask in range(33):
    try:
        net = ip_network("111.81.27.192/" + str(mask), True)

        if ip_address("111.81.27.208") in net:
            minByte = min(minByte, int(str(net.netmask).split('.')[3]))
    except:
        _ = 1
print(minByte)
