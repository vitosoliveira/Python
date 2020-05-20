casas = int(input("Numero das casas: "))
x = 0
comp = []
while x < casas:
    x += 1
    n = input("entrada 1: ")
    comp.append(n)
    for w in comp:
        if w in "um" or "dois" or "tres":
            print(comp)