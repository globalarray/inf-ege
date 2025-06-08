f = open("22_08.txt", 'r').readlines()

procTimes = dict()

def set_running_time(pData):
    idx = int(pData[0])
    selfTime = int(pData[1])

    if idx in procTimes:
        return

    if pData[2] == '0':
        procTimes[idx] = selfTime
        return

    dependProcIds = map(int, pData[2].split(';'))

    time = 0

    for dpdId in dependProcIds:
        if dpdId not in procTimes:
            set_running_time(f[dpdId].split())
        time = max(time, procTimes[dpdId])

    procTimes[idx] = time + selfTime

for line in f[1:]:
    set_running_time(line.split())

r = 0

for i in range(max(procTimes.values())+1):
    cnt = 0

    for procId, procEndTime in procTimes.items():
        procStartTime = procEndTime - int(f[procId].split()[1])

        if procStartTime <= i < procEndTime:
            cnt += 1
    if cnt == 4:
        r += 1
print(r)
