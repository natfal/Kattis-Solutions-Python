nums = []
limit = int(input())

for x in range(limit):
    nums.append(int(input()))

nums.reverse()
print(*nums, sep = "\n")