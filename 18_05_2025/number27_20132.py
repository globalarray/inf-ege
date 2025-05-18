from math import dist

f = open("27A_1_20132.txt")

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

def distance(cluster1, cluster2):
    m = []

    for p1 in cluster1:
        for p2 in cluster2:
            m.append([dist(p1, p2), [p1, p2]])
    return min(m)[1]

dists = []

for i in range(len(clusters)-1):
    for j in range(i+1, len(clusters)):
        dists.append(distance(clusters[i], clusters[j]))

Px = int((sum([x for d in dists for x,y in d]) / (len(dists) * 2)) * 10000)
Py = int((sum([y for d in dists for x,y in d]) / (len(dists) * 2)) * 10000)

print(Px, Py)
