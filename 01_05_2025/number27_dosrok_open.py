from math import dist

f = open("27_B_21911.txt", 'r')

f.readline()

data = []

for line in f:
    data.append([float(x) for x in line.replace(",", ".", -1).split()])

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

    clusters.append(cluster)

print(len(clusters))

def centroid(cluster):
    m = []

    for p in cluster:
        m.append([sum(dist(p, p1) for p1 in cluster), p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]

Px = int((sum(x for x, y in centroids) / len(centroids)) * 10000)
Py = int((sum(y for x, y in centroids) / len(centroids)) * 10000)

print(Px, Py)
