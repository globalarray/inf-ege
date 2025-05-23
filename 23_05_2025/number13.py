from ipaddress import ip_network, ip_address

r = 0

for i in range(33):
    try:
        net = ip_network("84.23.84.0/" + str(i), True)

        if ip_address("84.23.84.23") in net:
            msk = str(net.netmask).split('.')

            r = max(int(msk[2]) + int(msk[3]), r)
    except:
        pass
print(r)
