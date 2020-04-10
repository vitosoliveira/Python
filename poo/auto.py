class CarroCorrida:
    __numero_carro = None
    __nome_piloto = None
    __velocidade_max = None
    __velocidade_atual = None
    __ligado = None

    def __init__(self, vel_max):
        self.__ligado = False
        self.__velocidade_atual = 0.0
        self.__velocidade_max = vel_max

    def get_numero_carro(self):
        return self.__numero_carro

    def get_nome_piloto(self):
        return self.__nome_piloto

    def get_velocidade_max(self):
        return self.__velocidade_max

    def get_velocidade_atual(self):
        return self.__velocidade_atual

    def get_ligado(self):
        return self.__ligado

    def set_numero_carro(self, numero):
        self.__numero_carr = numero

    def set_nome_piloto(self, nome):
        self.__nome_piloto = nome

    def set_velocidade_max(self, max):
        self.__velocidade_max = max

    def set_velocidade_atual(self, status):
        self.__velocidade_atual = status

    def set_ligado(self, ligado):
        self.__ligado = ligado

    def ligar(self):
        if self.__ligado == False:
            self.__ligado == True
            print("Carro ligado")
        else:
            print("Ö carro ja esta ligado")

    def desligar(self):
        if self.__ligado == True and self.__velocidade_atual == 0:
            self.__ligado == False
            print("Carro desliago")
        elif self.__velocidade_atual != 0:
            print("Pare primeiro")
        else:
            print("O carra ja estava desligado")

    def max(self, n):
        if self.__ligado == True:
            if self.__velocidade_atual + n > self.__velocidade_max:
                self.__velocidade_atual = self.__velocidade_max
            else:
                self.__velocidade_atual += n
        else:
            print("O carro desligado não acelera")

    def frear(self):
        if self.__ligado == True and self.__velocidade_atual != 0:
            self.__velocidade_atual = 0
            print("Carro ka esta parado")
        elif self.__ligado == True and self.__velocidade_atual == 0:
            print("Carro ja freado")
        else:
            print("Carro desligado")
