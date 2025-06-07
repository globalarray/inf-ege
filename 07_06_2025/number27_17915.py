from math import dist

f = open("27_A_17915.txt", 'r')

f.readline()

data = []

for line in f:
    data.append([float(x) for x in line.replace(",", ".").split()])

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
    cl = get_cluster(data[0])

    clusters.append(cl)
print(len(clusters))

def centroid(c):
    m = []

    for p in c:
        m.append([sum(dist(p, p1) for p1 in c), p])
    return min(m)[1]

centroids = [centroid(cls) for cls in clusters]

Px = int(sum(x for x,y in centroids) / len(centroids) * 10000)
Py = int(sum(y for x,y in centroids) / len(centroids) * 10000)

print(Px, Py)
