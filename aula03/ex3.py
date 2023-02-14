def maximo(n1, n2):
    if n1>=n2:
        return n1
    else:
        return n2


def main():
    x = input("Primeiro número:")
    y = input("Segundo número:")
    print(maximo(x, y))

main()