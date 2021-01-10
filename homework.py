groups = input().split(";", -1)
count = 0

for x in groups:
    if (x.find("-") >= 0):
        nums = list(map(int, x.split("-", -1)))
        count = count + (nums[1] - nums[0] + 1)
    else:
        count = count + 1

print(count)