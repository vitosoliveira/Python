##heruku
##travis
##faça um prigrama que exiba os 100 primeiros numeros primos
##branch

n = 2
div = 0
primo = ""
x=0
l=100
while x < l:
    div = 0
    for i in range (1,n+1):
        if n % i == 0:
            div += 1
    if div ==  2:
        primo = primo + str(n) + ','
        x += 1
    div = 0
    n += 1
primo = primo[0:len(primo)]
print (primo)


                

