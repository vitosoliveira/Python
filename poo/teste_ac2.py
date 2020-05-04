from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, titular, agencia, conta, saldo):
        self.__titular = titular
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def transferir(self, valor, conta_destino):
        pass


class ContaCorrente(Conta):
    def __init__(self, titular, agencia, conta, saldo, limite):
        super().__init__(titular, agencia, conta, saldo)
        self.__limite = limite

    def get_saldo(self):
        return self._Conta__saldo

    def depositar(self, valor):
        if valor > 0:
            self._Conta__saldo += valor
        else:
            raise ValueError("Impossivel")

    def sacar(self, valor):
        total = self._Conta__saldo + self.__limite
        if total > 0:
            w = total - valor
            if w < 0:
                raise ValueError("SALDO INSUFICIENTE")
            else:
                total -= valor

    def transferir(self, valor, conta_destino):
        if self._Conta__saldo > 0:
            w = self._Conta__saldo - valor
            if w < 0:
                raise ValueError("SALDO INSUFICIENTE")
            else:
                self._Conta__saldo -= valor
                conta_destino._Conta__saldo += valor


class ContaPoup(Conta):
    def __init__(self, titular, agencia, conta, saldo):
        super().__init__(titular, agencia, conta, saldo)

    def get_saldo(self):
        return self._Conta__saldo

    def depositar(self, valor):
        if valor > 0:
            self._Conta__saldo += valor
        else:
            raise ValueError("Impossivel")

    def sacar(self, valor):
        if self._Conta__saldo > 0:
            w = self._Conta__saldo - valor
            if w < 0:
                raise ValueError("SALDO INSUFICIENTE")
            else:
                self._Conta__saldo -= valor

    def transferir(self, valor, conta_destino):
        if self._Conta__saldo > 0:
            w = self._Conta__saldo - valor
            if w < 0:
                raise ValueError("SALDO INSUFICIENTE")
            else:
                self._Conta__saldo -= valor
                conta_destino._Conta__saldo += valor

    def calcular_rendimento(self, taxa):
        self._Conta__saldo += (self._Conta__saldo*taxa/100)


class ContaInvestimento(Conta):
    def __init__(self, titular, agencia, conta, saldo):
        super().__init__(titular, agencia, conta, saldo)
        self.__taxa_adm = 3

    def get_saldo(self):
        return self._Conta__saldo

    def depositar(self, valor):
        if valor > 0:
            self._Conta__saldo += valor
        else:
            raise ValueError("Impossivel")

    def sacar(self, valor):
        if self._Conta__saldo > 0:
            w = self._Conta__saldo - valor
            if w < 0:
                raise ValueError("SALDO INSUFICIENTE")
            else:
                self._Conta__saldo -= valor

    def transferir(self, valor, conta_destino):
        if self._Conta__saldo > 0:
            w = self._Conta__saldo - valor
            if w < 0:
                raise ValueError("SALDO INSUFICIENTE")
            else:
                self._Conta__saldo -= valor
                conta_destino._Conta__saldo += valor

    def calcular_rendimento(self, taxa):
        self._Conta__saldo += (self._Conta__saldo * (taxa / 100)) - \
            (self._Conta__saldo * (self.__taxa_adm/100))


primeira = ContaPoup("Vitor", 123, 111111, 200)
segundo = ContaCorrente("Gabs", 456, 222222, 10000, 200)
terceiro = ContaInvestimento("Vini", 12358, 20000, 1)
primeira.transferir(30, segundo)
terceiro.calcular_rendimento(10)
print(terceiro.get_saldo())

