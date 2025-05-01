from math import dist

f = open("27.19.B_20497.txt", 'r')

data = []

for line in f:
    data.append([float(x) for x in line.split()])

def get_cluster(p0):
    cluster = [p for p in data if dist(p0, p) < 2]

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
print(len(clusters))

def edger(cluster):
    m = []

    for p in cluster:
        m.append([sum(dist(p, p1) for p1 in cluster), p])
    return max(m)[1]

edgers = [edger(cluster) for cluster in clusters]

Tx = int((sum(x for x, y in edgers) / len(edgers)) * 10000)
Ty = int((sum(y for x, y in edgers) / len(edgers)) * 10000)

print(Tx, Ty)
