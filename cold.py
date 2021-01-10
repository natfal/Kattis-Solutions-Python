input()
nums = map(int, input().split())
count = 0

for x in nums:
    if x < 0:
        count = count + 1

print(count)