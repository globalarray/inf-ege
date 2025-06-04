from math import dist

f = open("27B_18630.txt")
f.readline()

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
    cls = get_cluster(data[0])

    if len(cls) > 10:
        clusters.append(cls)
print(len(clusters))

def centroid(cl):
    m = []

    for p in cl:
        m.append([sum(dist(p, p1) for p1 in cl), p])
    return min(m)[1]

centroids = [centroid(c) for c in clusters]

Px = int(sum(x for x,y in centroids) / len(centroids) * 100000)
Py = int(sum(y for x,y in centroids) / len(centroids) * 100000)

print(Px, Py)
