gotAway = True
s = ""

for x in range(5):
    if input().find("FBI") >= 0:
        gotAway = False
        s = s + str(x + 1) + " "

if gotAway:
    print("HE GOT AWAY!")
else:
    print(s.strip())
