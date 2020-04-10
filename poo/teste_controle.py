import controle

elevador1 = controle.Elevador(5,[0,1,2,3,4,5])
elevador2 = controle.Elevador(5,[0,6,7,8,9,10])



elevador1.set_quantidade_pessoas(0)
elevador1.entrar() #1
elevador1.entrar() #2
elevador1.entrar() #3
elevador1.entrar() #4
elevador1.entrar() #5
elevador1.entrar()

elevador2.set_quantidade_pessoas(0)
elevador2.entrar() #1
elevador2.entrar() #2 
elevador2.entrar() #3
elevador2.entrar() #4
elevador2.entrar() #5
elevador2.entrar()



elevador1.set_quantidade_pessoas(50)
elevador1.sair()



#3elevador1.descer()
#3elevador2.descer()