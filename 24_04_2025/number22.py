f = open("22_21715.txt", 'r').readlines()

procTimes = dict()

def setRunningTime(pcData):
    id = int(pcData[0])
    selfTime = int(pcData[1])

    if id in procTimes:
        return

    if pcData[2] == '0':
        procTimes[id] = selfTime
        return

    dependProcIds = map(int, pcData[2].split(';'))

    time = 0

    for dependProcId in dependProcIds:
        if dependProcId not in procTimes:
            setRunningTime(f[dependProcId-100].split())
        time = max(time, procTimes[dependProcId])

    procTimes[id] = selfTime + time

for i in range(1, len(f)):
    setRunningTime(f[i].split())

print(max(procTimes.values()))
