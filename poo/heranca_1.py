class Animal:

    def __init__(self, nome, comprimento, numero_patas, cor, velocidade_media):
        self.nome = nome
        self.comprimento = comprimento
        self.numero_patas = numero_patas
        self.cor = cor
        self.velocidade_media = velocidade_media

    def exibe(self):
        print(self.nome)
        print(self.comprimento)
        print(self.numero_patas)
        print(self.cor)
        print(self.velocidade_media)


croco = Animal("Croco", "1.20", 4, "Verde", 120)
croco.exibe()


class Peixe(Animal):

    def __init__(self, nome, comprimento, numero_patas, cor, velocidade_media, caracteristica):
        super().__init__(nome, comprimento, numero_patas, cor, velocidade_media)
        self.caracteristica = caracteristica
    
    def exibir_peixe(self):
        super().exibe()
        print(self.caracteristica)


pirarucu = Peixe("Pirarucu", 1, 0, "branco", 50, "Peixe")
pirarucu.exibir_peixe()
