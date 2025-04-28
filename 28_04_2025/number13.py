from ipaddress import ip_network, ip_address

m = 10**10

for i in range(1, 33):
    try:
        net = ip_network("84.32.84.32/" + str(i), False)

        if ip_address("84.32.84.32") in net:
            if f'{net[-2]:b}'.count('1') == 19:
                m = min(m, f'{net.netmask:b}'.count('1'))
    except:
        _ = 1
print(m)
