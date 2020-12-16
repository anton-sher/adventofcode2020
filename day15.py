nums = [8,11,0,19,1,2]

while(len(nums) < 2020):
    last = nums[-1]
    for i in range(2, len(nums) + 1):
        if nums[-i] == last:
            nums.append(i - 1)
            break
    else:
        nums.append(0)

print(nums[2020 - 1])

numsp = dict()
numsd = dict([(v, i) for (i, v) in enumerate(nums)])

n = len(nums)
l = nums[-1]

while n < 30000000:
    if l in numsp:
        l = numsd[l] - numsp[l]
    else:
        l = 0
    if l in numsd:
        numsp[l] = numsd[l]
    numsd[l] = n
    n += 1

print(l)
