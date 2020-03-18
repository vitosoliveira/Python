numero=int(input("Digite um numero:"))
divisor = []
for div in range (1,numero+1):
    if numero%div == 0:
        divisor.append(div)
print(divisor)


