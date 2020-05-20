#Nome: Vitor Soares De Oliveira RA:1901878
#Nome: Henrique Marinho de Almeida RA:1901772

#Nome: Vitor Soares De Oliveira RA:1901878
#Nome: Henrique Marinho de Almeida RA:1901772

from abc import ABC, abstractmethod


class Parte (ABC):

    def __init__(self, codigo, nome, desc, valor):
        self.__codigo = int(codigo)
        self.__nome = nome
        self.__desc = desc
        self.__valor = float(valor)

    @abstractmethod
    def calcular_valor(self):
        pass

    @abstractmethod
    def exibir(self):
        pass


class Parafuso(Parte):
    comprimento = float
    diametro = float

    def __init__(self, codigo, nome, desc, valor, comprimento, diametro):
        super().__init__(codigo, nome, desc, valor)
        self.__comprimento = float(comprimento)
        self.__diametro = float(diametro)

    def calcular_valor(self):
        return self._Parte__valor

    def exibir(self):
        print("Codigo: ", self._Parte__codigo)
        print("Nome: ", self._Parte__nome)
        print("Descrição: ", self._Parte__desc)
        print("Valor: ", self._Parte__valor)
        print("Comprimento: ", self.__comprimento)
        print("Diametro: ", self.__diametro)


class Motor(Parte):
    potencia = float
    corrente = float
    rpm = int

    def __init__(self, codigo, nome, desc, valor, potencia, corrente, rpm):
        super().__init__(codigo, nome, desc, valor)
        self.__potencia = float(potencia)
        self.__corrente = float(corrente)
        self.__rpm = int(rpm)

    def calcular_valor(self):
        return self._Parte__valor

    def exibir(self):
        print("Codigo: ", self._Parte__codigo)
        print("Nome: ", self._Parte__nome)
        print("Descrição: ", self._Parte__desc)
        print("Valor: ", self._Parte__valor)
        print("Potencia: ", self.__potencia)
        print("Correte: ", self.__corrente)
        print("RPM: ", self.__rpm)


class Item:

    def __init__(self, referencia_objeto, quantidade):
        self.__referencia_objeto = referencia_objeto
        self.__quantidade = int(quantidade)

    def calcular_valor(self):
        return self.__quantidade*self.__referencia_objeto._Parte__valor

parafu = Parafuso(50,"vitor","aaa",200,5,10)
parafu2 = Parafuso(5026,"vitor","aaa",523,501,200)

parafuitem = Item(parafu,50)

print("aaaa", parafuitem.calcular_valor())


print("trouxa",parafu._Parte__valor)
print(parafu.calcular_valor())
