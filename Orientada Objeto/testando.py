class Aluno:
    def _init_(self,arquivo):
        A = open ('entrada.txt',"r")
        arquivo = A.read()
        L = arquivo.split("\n")
        Nome = L[0]
        RA = L[1]
        AC1 = float(L[2])
        AC2 = float(L[3])
        AC3 = float(L[4])
        AC4 = float(L[5])
        AC5 = float(L[6])
        descarte = float (min(L))
        Nota_prova = float(L[7])
        Faltas = float(L[8])
        A.close()

    def calcular_situacao(arquivo):
        MAC = (((AC1+AC2+AC3+AC4+AC5-descarte)*0.5)/4 + (Nota_prova *0.5))
        Media_Faltas =(((60-Faltas)/60)*100)
        if MAC >=6:
            if Media_Faltas >= 80:
                situacao_final = ("Aprovado")
            else:
                situacao_final = ("Reprovado")
        else:
            situacao_final = ("Reprovado")

    def escrever_situacao(self,arquivo):
        self.novo_arquivo = open("situacao.txt","w")
        self.novo_arquivo.write(RA + " : "+ Nome + "\n")
        self.novo_arquivo.write(("%.1f" %MAC) + " \n")
        self.novo_arquivo.write(("%.1f" %Media_Faltas) + "%" +"\n")
        self.novo_arquivo.write((situacao_final) + " \n")
        self.novo_arquivo.close()


eu = Aluno("teste.txt")