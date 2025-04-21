from math import dist

f = open("27B_20971.txt", 'r')

data = []

for line in f:
    data.append([float(x) for x in line.split()])

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
    cluster = get_cluster(data[0])

    if len(cluster) > 10:
        clusters.append(cluster)

def centroid(cluster):
    m = []

    for p in cluster:
        m.append([sum(dist(p, p1) for p1 in cluster), p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]

Px = int((sum(x for x, y in centroids) / len(centroids)) * 10000)
Py = int((sum(y for x, y in centroids) / len(centroids)) * 10000)

print(Px, Py)
