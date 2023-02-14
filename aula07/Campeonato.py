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

def golos(lista):
    for jogo in lista:
        erro = True
        while erro:
            try:
                n1=int(input("Golos da equipa 1 no jogo {}:".format(jogo)))
                n2 = int(input("Golos da equipa 2 no jogo {}:".format(jogo)))
            except:

    return jogo

def listajogos():
    games =[]
    while True:
        n = input("Nome Equipa:")
        n = n.strip()
        if n!="":
            games.append(n)
        else:
            break
    return games

def main():
    games = listajogos()
    lista = jogos(games)
    print(games)
    jogo = golos(lista)
main()