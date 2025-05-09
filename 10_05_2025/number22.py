from turtledemo.penrose import start

f = open("22_18584.txt", 'r').readlines()

procTimes = dict()

def set_running_time(procData):
    idx = int(procData[0])
    selfTime = int(procData[1])

    if idx in procTimes:
        return

    if procData[2] == '0':
        procTimes[idx] = selfTime
        return

    dependProcIds = map(int, procData[2].split(';'))

    time = 0

    for dependProcId in dependProcIds:
        if dependProcId not in procTimes:
            set_running_time(f[dependProcId - 1000].split())
        time = max(time, procTimes[dependProcId])
    procTimes[idx] = selfTime + time

for line in f[1:]:
    set_running_time(line.split())

r = 0

for i in range(0, max(procTimes.values())+1):
    cnt = 0

    for procId, procEndTime in procTimes.items():
        selfTime = int((f[procId - 1000].split())[1])

        startTime = procEndTime - selfTime

        if startTime <= i < procEndTime:
            cnt += 1
    if cnt == 4:
        r += 1
print(r)
