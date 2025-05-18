from math import dist

f = open("27A_20130.txt")

data = []

for line in f:
    data.append([float(x) for x in line.replace(",", ".").split()])

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) < 1]

    if cluster:
        for p in cluster:
            data.remove(p)
        next_clusters = [get_cluster(p) for p in cluster]

        cluster += sum(next_clusters, [])
    return cluster

clusters = []

while data:
    cl = get_cluster(data[0])

    clusters.append(cl)
print(len(clusters))

def diogonal(cluster):
    m = []

    for p in cluster:
        for p2 in cluster:
            m.append([dist(p, p2), [p, p2]])
    return max(m)[1]

digs = [diogonal(cluster) for cluster in clusters]

Px = int((sum([x for d in digs for x, y in d]) / (len(digs) * 2)) * 10000)
Py = int((sum([y for d in digs for x, y in d]) / (len(digs) * 2)) * 10000)

print(Px, Py)
