from math import dist

f = open("27A_20294.txt", 'r')

data = []

for line in f:
    data.append([float(x) for x in line.split()])

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

def f(cluster):
    m = []

    for p in cluster:
        k = len([p1 for p1 in cluster if dist(p, p1) <= 1])

        m.append([k, p])
    return min(m)[1]

iz = [f(cluster) for cluster in clusters]

Px = int(abs(sum(x for x, y in iz)/len(iz)) * 100000)
Py = int(abs(sum(y for x, y in iz)/len(iz)) * 100000)

print(Px, Py)
