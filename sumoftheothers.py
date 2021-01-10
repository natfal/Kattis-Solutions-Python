while True:
    try:
        print(int(sum(list(map(int, input().split(" ",-1)))) / 2))
    except:
        break
