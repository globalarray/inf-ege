from fnmatch import fnmatch

nch = "13579"
ch = "02468"

for i in range(0, 10**8, 153):
    if i == 0: continue

    if fnmatch(str(i), "1*2?3*45"):
        nStr = str(i)[1:]

        ok = True

        trIdx = 0

        for idx, c in enumerate(nStr):
            if c not in nch:
                if not (c == "2" and nStr[idx+2] == "3"):
                    ok = False
                trIdx = idx + 2
                break

        if not ok:
            continue

        if nStr[trIdx-1] not in ch:
            continue

        gStr = nStr[trIdx:]

        for idx, c in enumerate(gStr):
            if c not in nch:
                if not (c == "4" and gStr[idx+1] == "5" and idx+1 == (len(gStr)-1)):
                    ok = False
                break
        if ok:
            print(i, i // 153)
