modulos = set()

while True:
    try:
        modulos.add(int(input()) % 42)
    except:
        break

print(len(modulos))

