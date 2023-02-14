with open('Lusiadas.txt', 'r', encoding='utf8') as f:
    letras = {}
    for linha in f:
        for car in linha:
            if car.isalpha():
                car = car.lower()
                if car not in letras:
                    letras[car]= 1
                else:
                    letras[car] +=1

    print(letras)