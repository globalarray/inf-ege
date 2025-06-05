from fnmatch import fnmatch

for i in range(0, 10**12, 84318):
    if i == 0: continue

    if fnmatch(str(i), "5*7?") and len(str(i)) == len(set(str(i))):
        print(i, i//84318)
