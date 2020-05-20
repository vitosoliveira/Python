primeira = []
segunda = []
terceira = []

primeira_lista = int(input("Tamanho Primeira Lista: "))
for x in range (primeira_lista):
    primeira_lista = int(input("Numeros da lista: "))
    primeira.append(primeira_lista)
segunda_lista = int(input("Tamanho Segunda lista: "))
for i in range (segunda_lista):
    segunda_lista = int(input("Numeros Segunda Lista: "))
    segunda.append(segunda_lista)
for y in primeira:
    for w in segunda:
        if y == w:
            terceira.append(w)

print(terceira)