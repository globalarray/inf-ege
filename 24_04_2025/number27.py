from math import dist

f = open("27_B_21425.txt", 'r')

data = []

for line in f:
    data.append([float(x) for x in line.replace(',', '.', -1).split()])

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) < 5]

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

from turtle import *
tracer(0)
screensize(2000, 2000)

k=10

for cluster in clusters:
    for x, y in cluster:
        setpos(x*k, y*k)
        dot(4, 'black')
update()
done()

def centroid(cluster):
    m = []

    for p in cluster:
        m.append([sum(dist(p, p1) for p1 in cluster), p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]

Px = int(sum(x for x, y in centroids) / len(centroids) * 10000)
Py = int(sum(y for x, y in centroids) / len(centroids) * 10000)

print(abs(Px), abs(Py))
