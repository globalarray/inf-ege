def f(x, m, history):
    if x > 40:
        return m % 2 == 0
    if m == 0: return 0

    h = []

    if len(history) == 0:
        h = [f(x + 3, m - 1, {m: "+3"}), f(x + 6, m - 1, {m: "+6"}), f(x * 2, m - 1, {m: "*2"})]
    else:
        if history[m+1] != "+3":
            history[m] = "+3"
            h.append(f(x + 3, m - 1, history))
        if history[m+1] != "+6":
            history[m] = "+6"
            h.append(f(x + 6, m - 1, history))
        if history[m+1] != "*2":
            history[m] = "*2"
            h.append(f(x * 2, m - 1, history))

    return any(h) if m % 2 != 0 else all(h)
print([s for s in range(2, 37) if f(s, 2, [])])
print([s for s in range(2, 37) if not(f(s, 1, [])) and f(s, 3, [])])
print([s for s in range(2, 37) if not(f(s, 2, [])) and f(s, 4, [])])
