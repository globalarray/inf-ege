f = list(map(int, open("17_7619.txt", 'r').readlines()))

def is_suit(n):
    return len(str(abs(n))) == 2

maxSuitableElement = max(list(filter(is_suit, f)))

cnt = 0
maxSum = 0

for i in range(len(f)-1):
    nums = [f[i], f[i+1]]

    if len(list(filter(is_suit, nums))) == 1:
        s = sum(nums)

        if s % maxSuitableElement == 0:
            cnt += 1
            maxSum = max(s, maxSum)
print(cnt, maxSum)
