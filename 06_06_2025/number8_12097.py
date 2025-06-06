from itertools import product

r = 0


for idx, word in enumerate(product('АГДИЛНРЯ', repeat=6)):
    if (idx + 1) % 2 == 0:
        if word[0] != 'Я' and word.count('Д') == 3:
            r = idx + 1
print(r)
