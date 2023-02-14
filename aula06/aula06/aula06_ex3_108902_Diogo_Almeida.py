# Complete o programa!

# a)
def loadFile(fname, lst):
    try:
        with open(fname , 'r') as file:
            line = file.readline()
            for line in file:
                lista = line.strip().split('\t')
                lista[0]=int(lista[0])
                lista[-3] = float(lista[-3])
                lista[-2]=float(lista[-2])
                lista[-1] = float(lista[-1])
                lst.append(tuple([lista[0],lista[1],lista[-3],lista[-2],lista[-1]]))
        return lst
    except:
        print("Ficheiro {} não existe!".format(fname))
        return lst
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    n1 = reg[2]
    n2 = reg[3]
    n3 = reg[4]
    media = (n1+n2+n3)/3
    return media

# c) Crie a função printPauta aqui...
def printPauta(lst,file):
    print("NUMERO{:^100}NOTA".format("NOME"))
    for reg in lst:
        print("{:>6}{:^100}{:4.1f}".format(reg[0],reg[1],notaFinal(reg)))
        file.write("{:>6}{:^190}{:4.1f}\n".format(reg[0],reg[1],notaFinal(reg)))

# d)
def main():
    lst = []
    # ler os ficheiros
    lst = loadFile("school1.csv", lst)
    lst = loadFile("school2.csv", lst)
    lst = loadFile("school3.csv", lst)
    lst = loadFile("sasd.csv", lst)
    # ordenar a lista
    lst.sort()
    # mostrar a pauta
    with open('pauta.txt','w') as file:
        printPauta(lst,file)

# Call main function
if __name__ == "__main__":
    main()