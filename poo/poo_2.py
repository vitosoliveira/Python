import poo
class Carro:
    modelo = None
    cor = None
    ano = None
    marco = None
    velo_atual = 0
    def __init__(self,proprietario):
        self.proprietario = proprietario
    def acelerar (self):
        self.velo_atual += 1
    def freiar (self):
        self.velo_atual = 0

end = poo.Endereco("Rua dos bobos",1235)
prop1 = poo.Proprietario("jorge",123,569,end)
carro1 = Carro(prop1)

print(carro1.proprietario.nome)
print(carro1.proprietario.endereco.get_rua())