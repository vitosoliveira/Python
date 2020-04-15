# Atividade Contínua 3
# Vitor Soares De Oliveira - 1901878
# Italo Rodrigues Da Silva - 1901642


class Elevador:

    __andar_atual = 0
    __quantidade_pessoas = 0
    __atendidos = None

    def __init__(self, capacidade, andares):
        if 0 not in andares:
            andares.append(0)
        self.__capacidade = capacidade
        self.__atendidos = andares

    def get_atendidos(self):
        return self.__atendidos

    def get_quantidade_pessoas(self):
        return self.__quantidade_pessoas

    def get_andar_atual(self):
        return self.__andar_atual

    def set_atendidos(self, atendidos):
        self.__atendidos = atendidos

    def set_quantidade_pessoas(self, quantidade_pessoas):
        self.__quantidade_pessoas = quantidade_pessoas

    def set_andar_atual(self, andar_atual):
        self.__andar_atual = andar_atual

    def entrar(self):
        if self.__quantidade_pessoas < self.__capacidade:
            self.__quantidade_pessoas += 1
            self.__quantidade_pessoas

    def sair(self):
        if self.__quantidade_pessoas > 0:
            self.__quantidade_pessoas -= 1
            return self.__quantidade_pessoas
        else:
            return

    def subir(self):
        if self.__atendidos in self.__andares:
            self.__andar_atual += 1

    def descer(self):
        if self.__atendidos in self.__andares and self.__andar_atual > 0:
            self.__andar_atual -= 1

    def deslocar_para(self, andar):
        for x in self.__atendidos:
            if x == andar:
                self.__andar_atual = andar


class Predio:

    def __init__(self, andar_alto, andar_baixo, elevadores):
        lista_andar_predio = []
        lista_andar_elevadores = []
        if elevadores != []:
            self.__elevadores = elevadores
            self.__andar_alto = andar_alto
            self.__andar_baixo = andar_baixo
            for x in range(andar_baixo, andar_alto + 1):
                if x <= andar_alto and x >= andar_baixo:
                    lista_andar_predio.append(x)
            for y in range(len(elevadores)):
                lista_andar_elevadores.append(y)
        elif lista_andar_predio not in lista_andar_elevadores:
            raise ValueError()

    def chamar(self, andar):
        return

    def __embarque(self, indice_elevador):
        if indice_elevador in self.__elevadores:
            if self.__elevadores[indice_elevador].getandar_atual > 0:
                self.__elevadores[indice_elevador].entrar()

    def __desembarque(self, indice_elevador):
        if indice_elevador in self.__elevadores:
            if self.__elevadores[indice_elevador].getandar_atual <= 0:
                self.__elevadores[indice_elevador].set__quantidade_pessoas(0)

    #  Tentei fazer algumas coisas no chamar, mas toda vez que tentava algo dava erro entao apaguei para nao zerar a ac
    # Mas foi quase
    # Tive que refazer pq interpretei o exercicios errado