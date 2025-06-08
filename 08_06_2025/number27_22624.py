from math import dist

f = open("27B_22624.txt", 'r')

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
    c = get_cluster(data[0])

    if len(c) < 5:
        continue
    clusters.append(c)
print(len(clusters))

def centroid(cl):
    m = []

    for p in cl:
        m.append([sum(dist(p, p1) for p1 in cl), p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]

Px = abs((sum(x for x,y in centroids) / len(centroids) * 10000) // 1)
Py = abs((sum(y for x,y in centroids) / len(centroids) * 10000) // 1)

print(Px,Py)
