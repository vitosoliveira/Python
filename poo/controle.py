# Atividade Contínua 3
# Nome Completo 1 - RA
# Nome Completo 2 - RA

#primeiro elevador do 0 ate o 5
#segundo elevaodr do 0 ate o 10

class Elevador:
    __andar_atual = None
    __quantidade_pessoas = None

    def __init__(self, capacidade,atendidos = []):
        self.__capacidade = capacidade
        self.__atendidos = atendidos

    def get_quantidade_pessoas (self):
        return self.__quantidade_pessoas
    
    def get_andar_atual (self):
        return self.__andar_atual
    
    def set_quantidade_pessoas (self,quantidade_pessoas):
        self.__quantidade_pessoas = quantidade_pessoas

    def set_andar_atual (self, andar_atual):
        self.__andar_atual = andar_atual
    ##Corrigido-------------------------------------------------------
    def entrar(self): 
        self.__quantidade_pessoas += 1
        if self.__quantidade_pessoas > 5:
            print("sem espaco, Só pode 5 pessoas")
    
    def sair(self):
        self.__quantidade_pessoas -= 1
        if self.__quantidade_pessoas >= 0 and self.__quantidade_pessoas <=5 :
            print("Uma pessoa saiu")
            if self.__quantidade_pessoas == 0:
                print("elevador vazio")                                             
        if self.__quantidade_pessoas < 0 or self.__quantidade_pessoas > 5:         # 
            print("Impossivel tal ato")                                           #
        return                                                                    # 
    #Corrigido ------------------------------------------------------------------|
    
    
    #falta rever \/
    def subir(self):
        if self.__atendidos == [0,1,2,3,4,5]:
            if self.__andar_atual in self.__atendidos:
                if self.__andar_atual >= 0  and self.__andar_atual < 5:
                    print("Subiu um andar")
                else:
                    print("Andar invalido")
        if self.__atendidos == [0,6,7,8,9,10]:
            if self.__andar_atual in self.__atendidos and self.__andar_atual == 0:
                print("Subiu seis andares")
            elif self.__andar_atual >= 6 and self.__andar_atual < 10 and self.__andar_atual in self.__atendidos:
                print("subbiu um andar")
            else:
                print("Andar invalido")
    

    def descer(self):
        if self.__atendidos == [0,1,2,3,4,5]:
             if self.__andar_atual in self.__atendidos:
                if self.__andar_atual > 0 and self.__andar_atual <= 5:
                    print("desceu um andar")
             if self.__andar_atual not in self.__atendidos:
                print("andar incorreto")
        if self.__atendidos == [0,6,7,8,9,10]:
            if self.__andar_atual in self.__atendidos and self.__andar_atual == 0:
                print("Não é possivel descer mais, so subir")
            if self.__andar_atual == 6:
                print("Desceu ate o terreo")
            elif self.__andar_atual > 6 and self.__andar_atual <= 10:
                print("desceu um andar")
            elif self.__andar_atual not in self.__atendidos:
                print("andar incorreto")


        return

    def deslocar_para(self, andar):
        return


class Predio:

    def __init__(self, andar_alto, andar_baixo, elevadores):
        return

    def chamar(self, andar):
        return

    def __embarque(self, indice_elevador):
        return

    def __desembarque(self, indice_elevador):
        return