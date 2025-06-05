from math import dist

f = open("27B_22625.txt", 'r')

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
    cls = get_cluster(data[0])

    clusters.append(cls)
print(len(clusters))

def centroid_ant(cl):
    m = []

    for p in cl:
        m.append([sum(dist(p, p1) for p1 in cl), p])
    return [min(m)[1][0], max(m)[1][1]]

c = [centroid_ant(c) for c in clusters]

Px = int(sum(x for x,y in c) / len(c) * 10000)
Sy = int(sum(y for x,y in c) / len(c) * 10000)

print(Px, Sy)
