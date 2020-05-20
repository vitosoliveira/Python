tamanho = []

tamanho_lista = int(input("Tamanho da lista:  "))
for x in range (tamanho_lista):
    tamanho_lista = int(input("Numeros:"))
    tamanho.append(tamanho_lista)
b=int(input("Numero adicional: "))

menores = []
for i in tamanho:
    if i <b:
        menores.append(i)
print(menores)