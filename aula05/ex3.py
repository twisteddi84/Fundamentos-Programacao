def inputFloatList():
    lista=[]
    n = input("Números:")
    n2 = n.replace(".","")
    while True:
        if n=="":
            break
        elif n2.isdigit()==True:
            s = float(n)
            lista.append(s)
            n = input("Números:")
            n2 = n.replace(".", "")
        else:
            n=input("Números:")
            n2 = n.replace(".", "")
    return lista

def countLower(lst,v):
    lista2=[]
    for i in lst:
        if i<v:
            lista2.append(i)
    return lista2

def minmax(lst):
    max = lst[0]
    min = lst[0]
    for i in lst:
        if i<min:
            min = i
        elif i>max:
            max = i
    print("O maximo é {}".format(max))
    print("O minimo é {}".format(min))



def main():
    lista = inputFloatList()
    print(lista)
    v = float(input("Número:"))
    lista2 = countLower(lista,v)
    print("{} e tem {} números.".format(lista2,len(lista2)))
    minmax(lista)


main()