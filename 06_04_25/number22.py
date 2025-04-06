f = list(map(lambda l: l.split(), open("22.txt", 'r').readlines()[1:]))

procIdsMap = dict()

for i in range(len(f)):
    procIdsMap[int(f[i][0])] = i

procTimes = dict()

def setRunningTime(pData):
    procId = int(pData[0])

    if procId in procTimes:
        return

    selfTime = int(pData[1])

    if len(pData) < 3:
        procTimes[procId] = selfTime
        return

    dependProcs = list(map(int, pData[2].split(';')))

    time = 0

    for dependProcId in dependProcs:
        if not(dependProcId in procTimes):
            setRunningTime(f[procIdsMap[dependProcId]])
        time = max(time, procTimes[dependProcId])
    procTimes[procId] = time + selfTime + 3 #+3 потому что автор тупой хуесос пытается подловить

for data in f:
    setRunningTime(data)

p = sorted(procTimes.items(), key=lambda item: item[1])

print(p)
