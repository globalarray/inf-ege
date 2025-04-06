from ipaddress import ip_network, ip_address

minLen = 10**10

for mask in range(33):
    try:
        net = ip_network("93.138.160.0/" + str(mask))

        if ip_address("93.138.161.94") in net:
            minLen = min(minLen, (bin(int(net.netmask))[2:]).count('0'))
    except:
        _ = 1
print(minLen)
