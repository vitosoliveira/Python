#1. Cria uma Classe Pessoa, contendo os atributos encapsulados, com seus respectivos
#seletores (getters) e modificadores (setters), e ainda o construtor padrão e pelo menos
#mais duas opções de construtores conforme sua percepção. Atributos: String nome;
#String endereço; String telefone;

#2. Considere, como subclasse da classe Pessoa (desenvolvida no exercício anterior) a
#classe Fornecedor. Considere que cada instância da classe Fornecedor tem, para além
#dos atributos que caracterizam a classe Pessoa, os atributos valorCredito correspondente
#ao crédito máximo atribuído ao fornecedor) e valorDivida (montante da dívida para com
#o fornecedor). Implemente na classe Fornecedor, para além dos usuais métodos
#seletores e modificadores, um método obterSaldo() que devolve a diferença entre os
#valores dos atributos valorCredito e valorDivida. Depois de implementada a classe
#Fornecedor, crie um programa de teste adequado que lhe permita verificar o
#funcionamento dos métodos implementados na classe Fornecedor e os herdados da
#classe Pessoa.



class Pessoa():
    __telefone = ""
    def __init__(self,nome,endereco):
        self.__nome = nome
        self.__endereco = endereco
    def get_nome(self):
        return self.__nome
    def get_end(self):
        return self.__endereco
    def get_tel(self):
        return self.__telefone
    def set_nome (self,nome):
        self.__nome = nome
    def set_end (self, endereco):
        self.__endereco = endereco
    def set_tel (self,tel):
        self.__telefone = tel

class fornecedor(Pessoa):
    def __init__(self, nome, endereco, valorCredito,valorDivida):
        super().__init__(nome,endereco)
        self.__valorCredito = valorCredito
        self.__valorDivida = valorDivida
    def get_vlrCredito(self):
        return self.__valorCredito
    def set_vlrcredito(self,vlrCredito):
        self.__valorCredito = vlrCredito
    def get_vlrDivida(self):
        return self.__valorDivida
    def set_vlrDivida(self,vlrdivida):
        self.__valorDivida = vlrdivida
    def obterSaldo(self):
        valor = self.__valorDivida - self.__valorCredito
        if valor > 0:
            return 'Vc tem uma divida de: ',valor 
        else:
            return 'Vc não tem divida'

        

gabs = Pessoa("Gabriela","Rua marques 159")
gabs.set_tel("979532484")
print(gabs.get_nome())
print(gabs.get_tel())
print(gabs.get_end())

amil = fornecedor("AMIL","RUA DOS BOBOS",100,1000)
print(amil.obterSaldo())

