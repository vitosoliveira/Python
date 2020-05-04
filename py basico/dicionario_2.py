dic = {}
for x in range (0,2,1):
    cpf = int(input("cpf: "))
    nome = input("Nome: ")
    idade = int(input("idade: "))
    dic[cpf] = nome,idade
print(dic)