from math import dist

f = open("27B_20294.txt", 'r')

data = []

for line in f:
    data.append([float(x) for x in line.split()])

def get_cluster(p0):
    cluster = [p for p in data if dist(p0, p) < 0.4]

    if cluster:
        for p in cluster:
            data.remove(p)

        next_clusters = [get_cluster(p) for p in cluster]

        cluster += sum(next_clusters, [])
    return cluster

clusters = []

while data:
    cls = get_cluster(data[0])

    clusters.append(cls)

print(len(clusters))

def st(cl):
    m = []

    for p in cl:
        m.append([len([p1 for p1 in cl if dist(p, p1) < 1]), p])
    return min(m)[1]

stt = [st(c) for c in clusters]

Px = int(sum(x for x,y in stt) / len(stt) * 100000)
Py = int(sum(y for x,y in stt) / len(stt) * 100000)
print(abs(Px),abs(Py))
