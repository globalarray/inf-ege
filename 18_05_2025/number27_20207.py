from math import dist

f = open("27B_2_20207.txt", 'r')

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

def med(cluster):
    return [med_get(cluster, idx) for idx in range(2)]

def med_get(cluster, idx):
    for p in cluster:
        cnt = 0

        for p2 in cluster:
            if p[0] == p2[0] and p[1] == p2[1]:
                continue
            if p[idx] > p2[idx]:
                cnt += 1
        if cnt == (len(cluster)-1) / 2:
            return p[idx]

meds = [med(cluster) for cluster in clusters]

Px = int((sum(x for x,y in meds) / len(meds)) * 10000)
Py = int((sum(y for x,y in meds) / len(meds)) * 10000)

print(Px, Py)
