import math
##ponto vermelho pi^4
##valor de pi só mutiplicar por 
## toda vez que aparecer um ponto = tuple 
class Circulo:
    def __init__ (self, raio = float, centro = ()):
         self.raio = raio
         self.centro = centro

    def imprime_dados(self):
        print("raio: ",self.raio)
        print("centro: ", self.centro)
        ## Metodo que imprime os dados do circulo        

    def area (self):
        return math.pi*(self.raio)**2.0
        ##metodod que devolve a area do circulo 
   
    def perimetro(self):## tamanho do circulo
        return 2.0*math.pi*self.raio
     
        ## metodo que devolve o perimetro do ciruclo

    def dentro (self,ponto = ()):
        if distancia(ponto,self.centro) <= self.raio:
            return True
        elif distancia(ponto,self.centro) > self.raio:
            return False     
        ## Metodo que recebe     um ponto (tupla) e devolve 
            ## True, se o ponto esta dentro do circulo *
        ## Flase, caso contraio
        ## distacia entre dois pontos
def distancia (a = (), b = ()):
    return math.sqrt((a[1]-a[0])**2 + (b[1]-b[0]**2))
    ## funcao que recebe dois pontos tupla, a e b
    ## calcula e devolve a discian entre eles 