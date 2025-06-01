from math import dist

f = open("CG81D3Jp4.txt", 'r')

data = []

for line in f:
    data.append([float(x) for x in line.replace(',', '.').split()])

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

    clusters.append(cluster)

def median(cls, idx):
    for p in cls:
        b = 0
        for p2 in cls:
            if p[idx] == p2[idx]:
                continue
            if p[idx] > p2[idx]:
                b += 1
        if b == (len(cls)-1)//2:
            return p[idx]
meds = [[median(clust, 0), median(clust, 1)] for clust in clusters]

Px = int((sum(x for x,y in meds) / len(meds)) * 10000)
Py = int((sum(y for x,y in meds) / len(meds)) * 10000)

print(Px, Py)
