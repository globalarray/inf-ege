f = open("22_16267.txt", 'r').readlines()

procTimes = dict()

def set_running_time(pData):
    idx = int(pData[0])

    if idx in procTimes:
        return

    selfTime = int(pData[1])

    if pData[2] == '0':
        procTimes[idx] = selfTime
        return
    dependProcIds = map(int, pData[2].split(';'))

    time = 0

    for dependProcId in dependProcIds:
        if dependProcId not in procTimes:
            set_running_time(f[dependProcId].split())
        time = max(time, procTimes[dependProcId])

    procTimes[idx] = time + selfTime

for line in f[1:]:
    set_running_time(line.split())

for i in range(max(procTimes.values())+1):
    cnt = 0

    for procId, procEndTime in procTimes.items():
        procStartTime = procEndTime - int(f[procId].split()[1])

        if procStartTime <= i < procEndTime:
            cnt += 1
    print([i, cnt])
