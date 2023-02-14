def media():
    cont = 0
    n2 = 0
    while True:
        v = input("Valor Real:")
        if v == "":
            break
        else:
            n = float(v)
            cont +=1
            n2 = n2 + n
    return (n2/cont)

def main():
    resultado = media()
    print("A média entre os valores reais introduzidos é de {}.".format(resultado))

main()