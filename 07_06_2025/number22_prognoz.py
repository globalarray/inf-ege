f = open("22_07.txt", 'r').readlines()

procTimes = dict()

def set_running_time(pData, t):
    idx = int(pData[0])

    if pData[1] == 't':
        selfTime = t
    else:
        selfTime = int(pData[1])

    if idx in procTimes:
        return

    if pData[2] == '0':
        procTimes[idx] = selfTime
        return

    dependProcIds = map(int, pData[2].split(';'))

    time = 0

    for dependProcId in dependProcIds:
        if dependProcId not in procTimes:
            set_running_time(f[dependProcId - 200].split(), t)
        time = max(time, procTimes[dependProcId])
    procTimes[idx] = selfTime + time

for t in range(1000, 5000):
    for line in f[1:]:
        set_running_time(line.split(), t)
    if max(procTimes.values()) > 8432:
        break
    procTimes = dict()
print(t-1)
