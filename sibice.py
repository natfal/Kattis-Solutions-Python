import math

dims = list(map(int, input().split()))
largest = math.hypot(dims[1], dims[2]) # change this

for i in range(dims[0]):
    if int(input()) <= largest:
        print("DA")
    else:
        print("NE")