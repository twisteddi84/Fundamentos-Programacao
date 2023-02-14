n = int(input("Número inteiro:"))
cont = 1
soma = 0
if n<0:
    print("Número tem de ser positivo.")
    n=int(input("Numero inteiro"))
for x in range(1,n):
    if n%x==0:
        print("{} é divisor".format(cont))
        soma = soma + cont
        cont +=1
    else:
        cont +=1
if soma<n:
    print("Número deficiente pois {}<{}".format(soma,n))
elif soma==n:
    print("Número perfeito pois {}={}".format(soma, n))
else:
    print("Número abundante pois {}>{}".format(soma, n))