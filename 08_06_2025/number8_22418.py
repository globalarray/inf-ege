from itertools import product

r = 0

for idx, word in enumerate(product("ВДЁЖИНОРЯ", repeat=5)):
    if (idx + 1) % 2 == 0:
        if word[0] == word[-1] and word.count("Р") >= 2:
            r = idx + 1
print(r)
