def f(n):
    v = (hex(n)[2:]).replace("e", "0", -1)

    v = v[:len(v)-4]

    return len(list(filter(lambda x: int(x, 16) > 8, list(v))))

print(f((8**2024)*(4**2025)*(2**2026)-((8**11)*((16**310)-(16**209))+((2**12)*(2**12)))+(16**3011)))
