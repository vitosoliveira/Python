# DICA: a função uniform(a, b) do módulo random,
# gera um número aleatório no intervalo [a, b].

import random
import geometria
n = int(input("Quantos pontos quer usar para o teste: "))
c1 = geometria.Circulo(5,(0.0,0.0))
c1.imprime_dados()
print(c1.area())
print(c1.perimetro())
quad = (c1.raio*2) ** 2
pontos_dentro = 0

for i in range (n):
    x,y = random.uniform(0,5),random.uniform(0,5)
    a = (x,y) 
    ponto = c1.dentro((a))
    print(ponto)
    
    if ponto == True:
        pontos_dentro += 1
        print(pontos_dentro)
proporcao = pontos_dentro / n
estimativa = quad * proporcao
print(estimativa)
print(proporcao)


