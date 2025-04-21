f = list(map(lambda l: list(map(int, l.split())), open("9_21704.txt", 'r').readlines()))

for idx, nums in enumerate(f):
    if nums[6] <= nums[5] <= nums[4] <= nums[3] <= nums[2] <= nums[1] <= nums[0]:
        if ((nums[0] + nums[6]) / 2) > (sum(nums[1:6]) / 5):
            print(sum(nums))
            break
