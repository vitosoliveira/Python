##Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


nota = [10,5,9,10]
soma=0
for i in range(len(nota)):
    soma += nota[i]/len(nota)
print(soma)