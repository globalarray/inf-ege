f = open("26.txt", 'r').readlines()

eventCnt = int(f[0])

events = []

mTime = 0

for idx in range(eventCnt):
    evData = list(map(int, f[idx+1].split()))

    events.append(evData)
events.sort(key=lambda x: x[1])

l = []

for ev in events:
    if len(l) == 0 or ev[0] >= l[-1]:
        l.append(ev[1])
for ev in events:
    if ev[0] >= l[-2]:
        mTime = max(mTime, ev[1])
print(len(l))
print(mTime)
