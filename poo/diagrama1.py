from abc import ABC, abstractmethod


class Cadastro():
    def __init__(self, pessoas):
        self.__pessoas = pessoas

    def get_pessoas(self):
        return self.__pessoas

    def set_pessoas(self, pessoas):
        self.__pessoas = pessoas

    def cadastrar_pessoas(self, nome):
        self.set_pessoas = nome

    def exibir_cadastro(self):
        return self.__pessoas


class Data():
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


class Pessoa(ABC):
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data

    @abstractmethod
    def exibir_dados(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, data, salario):
        super().__init__(nome, data)
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def calcular_imposto(self):
        imp = self.__salario * 0.03
        return imp + self.__salario

    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("Data: ", self.data.dia, self.data.mes, self.data.ano)


datanasc = Data(25, 8, 1997)
func1 = Funcionario("Vitor", datanasc, 1250.5)
func1.exibir_dados()
