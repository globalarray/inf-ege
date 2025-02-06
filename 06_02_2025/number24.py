def parse_num(s, idx):
    num = ""
    while (idx < len(s)) and s[idx] in "0123456789":
        num += s[idx]
        idx += 1
    return num, idx

def parse_operation(s, idx):
    n, l = parse_num(s, idx)

    if idx == l:
        return False, idx

    idx = l

    if idx > len(s)-1:
        return False, idx

    if s[idx] in "*-":
        op = s[idx]
        idx += 1
    else:
        return False, idx

    n2, e = parse_num(s, idx)

    if e == idx:
        return False, idx

    idx = e

    if op == '*':
        return int(n) * int(n2), idx

    return int(n) - int(n2), idx

def parse_operation_two(n1, s, idx):
    if idx > len(s)-1:
        return False, idx

    if s[idx] in "*-":
        op = s[idx]
        idx += 1
    else:
        return False, idx

    n, l = parse_num(s, idx)

    if idx == l:
        return False, idx

    idx = l

    if op == "*":
        return n1 * int(n), idx

    return n1 - int(n), idx

f = open("24.txt").read()

result = 0
tmpLen = 0

i = 0

while i < len(f):
    if f[i] == 'B':
        tmpLen += 1
    else:
        if tmpLen != 0:
            c = f[i]
            ni = i

            r = 0

            val, newIdx = parse_operation(f, i)
            if val is not False:
                i = newIdx
                r += val

                while True:
                    
                    nr, j = parse_operation_two(r, f, i)
                    if nr is not False:
                        i = j
                        r = nr
                    else:
                        result = max(tmpLen+(i - ni), result)
                        tmpLen = 0
                        break
            else:
                tmpLen = 0
    i += 1
print(result)
