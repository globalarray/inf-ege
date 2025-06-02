from ipaddress import ip_network, ip_address

cnt = 0

for i in range(1, 33):
    try:
        net = ip_network("175.122.80.0/" + str(i), True)

        if ip_address("175.122.80.13") in net:
            if net.num_addresses >= 60:
                cnt += 1
    except:
        _ = 1
print(cnt)
