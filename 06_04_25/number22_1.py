f = list(map(lambda l: l.split(), open("06_04_22.txt", 'r').readlines()))

procTimes = dict()

def setRunningTime(pData):
    procId = int(pData[0])
    selfTime = int(pData[1])

    if procId in procTimes:
        return

    if pData[2] == '0':
        procTimes[procId] = selfTime
        return
    dependProcs = list(map(int, pData[2].split(';')))

    time = 0

    for dependProcId in dependProcs:
        if dependProcId not in procTimes:
            setRunningTime(f[dependProcId])
        time = max(time, procTimes[dependProcId])
    procTimes[procId] = selfTime + time

for i in range(1, len(f)):
    setRunningTime(f[i])
print(max(procTimes.values()))
