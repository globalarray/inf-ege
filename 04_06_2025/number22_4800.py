f = open("22_04.txt").readlines()

procTimes = dict()

def set_running_time(pData):
    idx = int(pData[0])
    selfTime = int(pData[1])

    if idx in procTimes:
        return
    if pData[2] == '0':
        procTimes[idx] = selfTime
        return

    dpdIds = map(int, pData[2].split(';'))

    time = 0

    for dependProcId in dpdIds:
        if dependProcId not in procTimes:
            set_running_time(f[dependProcId].split())

        time = max(time, procTimes[dependProcId])

    procTimes[idx] = time + selfTime

for line in f[1:]:
    set_running_time(line.split())

print(max(procTimes.values()))
