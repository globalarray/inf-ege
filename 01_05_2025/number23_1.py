from functools import lru_cache

@lru_cache(maxsize=None)  # неограниченный кэш
def f(x, y, c):
    if x > y or c > 28:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y, c + 1) + f(x + 2, y, c + 1) + f(x + 3, y, c + 1)

print(f(19, 100, 0))
