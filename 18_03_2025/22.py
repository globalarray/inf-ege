f = open("22.txt", 'r').readlines()

idToIdxMap = dict()

for idx, l in enumerate(f[1:]):
    idToIdxMap[int(l.split()[0])] = idx

procTimes = dict()

def setRunningTime(procData):
    id = int(procData[0])
    executionTime = int(procData[1])

    if id in procTimes:
        return

    if procData[2] == '0':
        procTimes[id] = executionTime
        return

    dependProcs = procData[2].split(';')

    time = 0

    for i in dependProcs:
        idx = int(i)
        if not(idx in procTimes):
            setRunningTime(f[idToIdxMap[idx]].split())
        time = max(time, procTimes[idx])
    procTimes[id] = executionTime + time

for l in f[1:]:
    setRunningTime(l.split())
print(max(procTimes.values()))
