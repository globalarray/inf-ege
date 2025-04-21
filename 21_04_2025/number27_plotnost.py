from math import dist

f = open("27A_20295.txt", 'r')

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
    cluster = get_cluster(data[0])

    if len(cluster) < 10:
        continue

    clusters.append(cluster)

def f(cluster):
    m = []

    for p in cluster:
        k = len([p1 for p1 in cluster if dist(p, p1) <= 1])

        m.append(k)
    return sum(m) / len(m)

funcs = [f(cluster) for cluster in clusters]

print(int(min(funcs) * 100000), int(sum(funcs) / len(funcs) * 100000))
