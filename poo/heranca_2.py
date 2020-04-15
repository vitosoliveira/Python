class funcionario:
    def __init__(self, nome, endereco, telefone, cpf, numero_ctps, salario):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf 
        self.numero_cpts = numero_ctps
        self.salario = salario
        

class Professor(funcionario):
    def __init__(self, nome, endereco, telefone, cpf, numero_ctps, salario, titulacao, area):
        super().__init__(nome, endereco, telefone, cpf, numero_ctps, salario)       
        self.titulacao = titulacao
        self.area = area
    def ministrar (self, curso):
        if curso == "ti":
            lista = ["lp2","bd","devops"]
            print(lista)
        else:
            print("curso errado")
        
        

class Tecnico(funcionario):
    def __init__(self, nome, endereco, telefone, cpf, numero_ctps, salario, cargo):
        super().__init__(nome, endereco, telefone, cpf, numero_ctps, salario)

class Aluno:
    def __init__(self, nome, disciplina):
        self.disciplina = disciplina
        self.nome = nome
    
    def controle(self):
        if self.disciplina == "ti":
            lista = ["lp2", "bd", "devops"]
            print("Suas aulas: ",lista)

class Disciplina:
    def __init__(self, nome, codigo, duracao):
        self.nome = nome
        self.codigo =  codigo
        self.duracao  = duracao

class Curso:
    def __init__(self, codigo, nome, duracao):
        self.codigo = codigo
        self.nome = nome
        self.duracao = duracao
prof = Professor("Jorge","Rua dos bobos",1122328490,47260258802,"0245645","R$600000","Doutor","TI")
prof.ministrar("ti")
eu = Aluno("Vitor","ti")
eu.controle()