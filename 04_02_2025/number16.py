def f(n):
    if n <= 2:
        return n + 1
    else:
        return 2 * f(n - 1) + f(n - 2)
print(f(4))
#https://inf-ege.sdamgia.ru/problem?id=5362
