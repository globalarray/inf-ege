from math import dist

f = open("27A_20130.txt", 'r')

data = []

for line in f:
    data.append([float(x) for x in line.replace(",", ".", -1).split()])

def get_cluster(p0):
    cluster = [p for p in data if dist(p0, p) < 1]

    if cluster:
        for p in cluster:
            data.remove(p)
        next_clusters = [get_cluster(p) for p in cluster]

        cluster += sum(next_clusters, [])
    return cluster

clusters = []

while data:
    cluster = get_cluster(data[0])

    if len(cluster) < 10:
        continue

    clusters.append(cluster)

def get_dioganal(cluster):
    maxPoints = []
    dst = -10**6

    for pIdx in range(len(cluster)-1):
        for p0Idx in range(pIdx+1, len(cluster)):
            p = cluster[pIdx]
            p1 = cluster[p0Idx]
            d = dist(p, p1)
            if d > dst:
                maxPoints = [p, p1]
                dst = d
    return maxPoints

diogonals = [get_dioganal(cluster) for cluster in clusters]

srx = 0
sry = 0

for dotsPerCluster in diogonals:
    for dot in dotsPerCluster:
        srx += dot[0]
        sry += dot[1]

Px = int(srx / (len(diogonals) * 2) * 10000)
Py = int(sry / (len(diogonals) * 2) * 10000)

print(Px, Py)
