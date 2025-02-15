s = list('8'*101)

s[0] = '1'
s[-1:] = '1'

s = "".join(s)

while ("81" in s) or ("882" in s) or ("8883" in s):
    if "81" in s:
        s = s.replace("81", '2', 1)
    elif "882" in s:
        s = s.replace("882", '3', 1)
    elif "8883" in s:
        s = s.replace("8883", '1', 1)
print(s)
