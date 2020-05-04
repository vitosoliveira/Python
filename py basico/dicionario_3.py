dic = {}
lista = []
for x in range (5):
    corredor = input("corredores: ")
    lista.append(corredor)
    dic[corredor] = []
    for i in range (4):
        volta = float(input("Volta : "))
        dic[corredor].append(volta)
    
    ##quem ganhou

t_min = 8000
for piloto in dic:
    temp = sum(dic[piloto]) ##soma todos os valores da lista
    if temp <t_min:
        t_min = temp
        nome = piloto
print("ganho com o tempo: ",nome,t_min)

volta_mininma_global = 500
for piloto in dic:
    volta_mininma_piloto = 500
    for volta in dic[piloto]:
        tenp = volta 
        if temp < volta_mininma_global:
            volta_mininma_global = volta_mininma_piloto
            nome = piloto 
    print("volta mais rapida", volta_mininma_global,nome)
