from math import dist

f = open("27_B (3).txt", 'r')

f.readline()

data = []

for line in f:
    data.append([float(x) for x in line.replace(",", ".").split()])

def get_cluster(p1):
    cluster = [p for p in data if dist(p1, p) < 5]

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

def centroid(c):
    m = []

    for p in c:
        m.append([sum(dist(p, p1) for p1 in c), p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]

Px = int(abs((sum(x for x,y in centroids) / len(centroids)) * 10000))
Py = int(abs((sum(y for x,y in centroids) / len(centroids)) * 10000))

print(Px, Py)
