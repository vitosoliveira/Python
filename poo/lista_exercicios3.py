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
