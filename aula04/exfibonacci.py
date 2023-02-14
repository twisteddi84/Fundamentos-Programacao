def fibo(n):
    n1=0
    n2=1
    cont=1
    while cont<=n:
        nr = n1 + n2
        print("{}º-->{}".format(cont,nr))
        n1 = n2
        n2 = nr
        cont+=1

def main():
    n=input("Introduza um número inteiro:")
    if n=="0":
        print("0º-->0")
    else:
        n=int(n)
        print("0º-->0")
        print(fibo(n))
main()
