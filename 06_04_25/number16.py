def g(n):
    if n == 1:
        return 1
    return g(n - 1) * n

def f(n):
    if n == 1:
        return 0
    return f(n - 1) + n
print(f(5) + g(5))
