from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 2:
        return 1
    elif n % 3 == 0:
        return 2024 + f(n - 2010)
    return 2025 + f(n // 3)

start = (2**20)+1

cnt = 0

while start < (2**21):
    v = f(start)

    if (v % 3 == 0 and str(v)[-1] == '3') or (v % 5 == 0 and str(v)[-1] == '5'):
        cnt += 1
    start += 1
print(cnt)
