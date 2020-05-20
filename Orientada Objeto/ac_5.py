class Aluno:
    def __init__(self, arquivo):
        self.arquivo = open(arquivo, 'r')
        linha = self.arquivo.read()
        palavra = linha.split("\n")
        self.nome = palavra[0]
        self.ra = palavra[1]
        self.nota_ac = []
        for x in palavra[2:6+1:1]:
            self.nota_ac.append(float(x))
        self.nota_prova = float(palavra[7])
        self.faltas = int(palavra[8])
        self.media = 0.0
        self.aprovado = False
        self.arquivo.close

    def calcular_aprovacao(self):
        a = min(self.nota_ac)
        self.nota_ac.remove(a)
        self.media = ((sum(self.nota_ac)/len(self.nota_ac)) +
                      (self.nota_prova))/2
        if self.media >= 6.0 and int(self.faltas) <= 20:
            self.aprovado = True
        else:
            self.aprovado = False
        return self.aprovado

    def set_media(self):
        a = min(self.nota_ac)
        self.nota_ac.remove(a)
        self.media = ((sum(self.nota_ac)/len(self.nota_ac)) +
                      (self.nota_prova))/2
        return self.media

    def escrever_situacao(self, nome_arquivo):
        arq = open(nome_arquivo, 'w')
        freq = ((60 - self.faltas)/60)*100
        arq.write(self.ra+':'+self.nome+"\n")
        arq.write(str("%.1f" % self.set_media() + "\n"))
        arq.write(str("%.1f" % freq)+"%"+"\n")
        if self.calcular_aprovacao() is True:
            arq.write("Aprovado")
        else:
            arq.write("Reprovado")
