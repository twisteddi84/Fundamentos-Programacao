def main():
    lista = []
    matches = []
    while True:
        n = input("Nome da equipa:")
        if n=="":
            break
        else:
            lista.append(n)
    print(lista)
    matches = jogos(lista)
    print("Todas as partidas entre essas equipas: {}.".format(matches))


def jogos(lista):
    matches=[]
    for i in lista:
        for x in lista:
            if i==x:
                True
            else:
                n = i,x
                matches.append(n)
    return matches

main()