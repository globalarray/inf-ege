f = open("22.txt", 'r').readlines()

procTimes = dict()

def setRunningTime(pData):
    id = int(pData[0])

    if id in procTimes:
        return
    selfTime = int(pData[1])

    if pData[2] == '0':
        procTimes[id] = selfTime
        return
    dependProcs = map(int, pData[2].split(';'))

    time = 0

    for dependProcId in dependProcs:
        if dependProcId not in procTimes:
            setRunningTime(f[dependProcId].split())
        time = max(time, procTimes[dependProcId])
    procTimes[id] = selfTime + time
for j in range(1, len(f)):
    setRunningTime(f[j].split())

for i in range(1, max(procTimes.values()) + 1):
    cnt = 0
    for procId, procTime in procTimes.items():
        selfTime = int((f[procId].split())[1])

        if procTime - selfTime <= i < procTime:
            cnt += 1
    if cnt == 3:
        print(i)
