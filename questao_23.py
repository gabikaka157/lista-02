
n1=int(input("digite sua primeira nota "))

n2=int(input("digite sua  segunda  nota "))

n3=n1+n2
n4=n3/2

if n4>7:
    print('ele ta aprovado {}'. format(n4))

elif n4 <7:

    print("reprovado {}". format(n4))

else :
    print ('ele ta reprovado')