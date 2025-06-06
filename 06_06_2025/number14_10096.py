from string import printable

for x in range(19):
    v = int("98897" + printable[x] + "21", 19) + int("2" + printable[x] + "923", 19)

    if v % 18 == 0:
        print(v // 18)
