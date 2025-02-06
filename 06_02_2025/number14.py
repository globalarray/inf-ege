def f(n, base):
    result = 0

    letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16,
               'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26,
               'R': 27, 'S': 28, 'T': 29, 'U': 30, 'Y': 31, 'W': 32, 'X': 33, 'V': 34, 'Z':35, 'a': 36}

    for idx, b in enumerate(n[::-1]):
        val = b
        if val in letters:
            val = letters[b]

        result += int(val) * (base**idx)
    return result

r = ""

for i in "0123456789ABCDEFGHIJKLMNOPQRSTUYWXVZa":
    if f("C59" + i + "BA98F", 37) * f("E3" + i + "5DA9C6", 37) % 36 == 0:
        r = i
print(f("2" + r + "1", 37))
