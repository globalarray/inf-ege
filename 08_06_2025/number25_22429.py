from math import isqrt

def is_simple(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def get_simple_divs(n):
    r = []

    for i in range(1, isqrt(n)+1):
        if n % i == 0:
            nums = [i, n // i]

            if nums[0] == nums[1]:
                nums = nums[1:]

            for g in nums:
                if is_simple(g):
                    r.append(g)
    return r

def f(n):
    return [x for x in get_simple_divs(n) if str(x)[-2:] == '17' and x != n and x != 17]

k = 0

for j in range(987653, 0, -1):
    v = f(j)

    if len(v) != 0:
        print(j, min(v))
        k += 1

        if k == 5: break
