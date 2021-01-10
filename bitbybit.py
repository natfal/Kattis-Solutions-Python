bits = []
instruction = []
bitAPos = ""
bitBPos = ""

def executeInstruct(word):
    if (word == "CLEAR"):
        bit_clear()
    if (word == "SET"):
        bit_set()
    if (word == "OR"):
        bit_or()
    if (word == "AND"):
        bit_and()

def bit_clear():
    bits[bitAPos] = '0'

def bit_set():
    bits[bitAPos] = '1'

def bit_or():
    if bits[bitAPos] == '1' or bits[bitBPos] == '1':
        bits[bitAPos] == '1'
    elif bits[bitAPos] == '?' or bits[bitAPos] == '?':
        bits[bitAPos] == '?'
    else:
        bits[bitAPos] == '0'

def bit_and():
    if bits[bitAPos] == '1' and bits[bitBPos] == '1':
        bits[bitAPos] == '1'
    elif bits[bitAPos] == '0' or bits[bitAPos] == '0':
        bits[bitAPos] == '0'
    else:
        bits[bitAPos] == '?'

while True:
    num = int(input())

    if (num == 0):
        break

    bits.clear()
    [bits.append("?") for x in range(32)]

    for x in range(num):
        myInstruction = input().split()
        # print(myInstruction[0])
        # print(myInstruction[1])
        bitAPos = 31 - int(myInstruction[1])
        try:
            bitBPos = 31 - int(myInstruction[2])
        except:
            pass
        executeInstruct(myInstruction[0])

    print(''.join(bits))