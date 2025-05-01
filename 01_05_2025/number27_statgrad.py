from math import dist

f = open("27_B_21599.txt", 'r')

data = []

for line in f:
    data.append([float(x) for x in line.replace(",", ".", -1).split()])

clA = [[], [], [], [], [], []]

for p in data:
    #p[0] - x ; p[1] - y
    x, y = p

    if y < -5:
        clA[0].append(p)
    elif y < x:
        clA[1].append(p)
    elif y < (1.5 * x) + 10:
        clA[2].append(p)
    elif x > -10:
        clA[3].append(p)
    elif y > (-2 * x) - 25:
        clA[4].append(p)
    else:
        clA[5].append(p)

def centroid(cluster):
    m = []

    for p in cluster:
        m.append([sum(dist(p, p1) for p1 in cluster), p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clA]

Px = int((sum(x for x, y in centroids) / len(centroids)) * 10000)
Py = int((sum(y for x, y in centroids) / len(centroids)) * 10000)

print(abs(Px), abs(Py))
