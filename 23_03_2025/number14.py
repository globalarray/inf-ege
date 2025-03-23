def convert(n, to):
    r = ""

    while n > 0:
        r += str(n % to)
        n //= to
    return r[::-1]

print(str(convert(3*(216**4)+2*(36**6)-648, 6)).count('5'))
