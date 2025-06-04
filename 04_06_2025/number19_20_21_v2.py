def f(x, m, last_step):
    if x > 40:
        return m % 2 == 0
    if m == 0: return 0

    h = []

    if last_step == "":
        h = [f(x + 3, m - 1, "+3"), f(x + 6, m - 1, "+6"), f(x * 2, m - 1, "*2")]
    else:
        if last_step != "+3":
            h.append(f(x + 3, m - 1, "+3"))
        if last_step != "+6":
            h.append(f(x + 6, m - 1, "+6"))
        if last_step != "*2":
            h.append(f(x * 2, m - 1, "*2"))

    return any(h) if m % 2 != 0 else all(h)
print([s for s in range(2, 37) if f(s, 2, "")])
print([s for s in range(2, 37) if not(f(s, 1, "")) and f(s, 3, "")])
print([s for s in range(2, 37) if not(f(s, 2, "")) and f(s, 4, "")])
