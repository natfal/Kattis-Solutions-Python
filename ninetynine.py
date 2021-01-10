required = [1, 1, 2, 2, 2, 8]

has = list(map(int, input().split()))

answer = []

[answer.append(required[i] - has[i]) for i in range(len(required))]

print(*answer, sep = " ")