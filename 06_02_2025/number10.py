f = open("p.txt").read()

convertedText = ""

for c in f:
    if not(c in ",!?.;()№\"»«:/"):
        convertedText += c

lines = convertedText.split('\n')

r = 0

for l in lines:
    words = l.split()

    for w in words:
        if len(w) == 0:
            continue
        if (w[0] == 'а' or w[0] == 'А') and (w[len(w)-1] == 'я'):
            if w in f and w.count('-') == 0:
                r += 1
print(r)

#https://imgur.com/a/JMfjKjo
