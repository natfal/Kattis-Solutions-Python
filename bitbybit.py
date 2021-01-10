bits = []
instruction = []
bitAPos = 0
bitBPos = 0

def executeInstruct(word):
    if (word == "CLEAR"):
        bit_clear()
    elif (word == "SET"):
        bit_set()
    elif (word == "OR"):
        bit_or()
    elif (word == "AND"):
        bit_and()

def bit_clear():
    bits[bitAPos] = '0'

def bit_set():
    bits[bitAPos] = '1'

def bit_or():
    if bits[bitAPos] == '1' or bits[bitBPos] == '1':
        bits[bitAPos] = '1'
    elif bits[bitAPos] == '?' or bits[bitBPos] == '?':
        bits[bitAPos] = '?'
    else:
        bits[bitAPos] = '0'

def bit_and():
    if bits[bitAPos] == '0' or bits[bitBPos] == '0':
        bits[bitAPos] = '0'
    elif bits[bitAPos] == '1' and bits[bitBPos] == '1':
        bits[bitAPos] = '1'
    else:
        bits[bitAPos] = '?'

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
        # print(bits[bitAPos])
        # print(bits[bitBPos])
        executeInstruct(myInstruction[0])
        # print(''.join(bits))
        # print(bitAPos)
        # print(bitBPos)
        # print(bits[bitAPos])
        # print(bits[bitBPos])

    print(''.join(bits))