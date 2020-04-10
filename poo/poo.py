class Proprietario:
    data_nasc = None
    endereco = None
    def __init__(self,nome,cpf,rg,endereco):
        self.nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.endereco = endereco 

class Endereco:
    rua = None
    bairro = None
    cidade = None
    estado  = None
    cep = 12358
    Complemento = None

    def __init__(self,rua,cep):
        self.__rua = rua
        self.__cep = cep
    
    def get_rua(self):
        return self.rua

    def set_complemento(self,complemento):
        self.__complemento = complemento
