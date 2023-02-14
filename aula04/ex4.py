def fatorial(n):
    f = 1
    for i in range(2, n + 1, 1):
        f = f*i
    return f


def main():
    n = int(input("Número inteiro:"))
    fat = fatorial(n)
    print(fat)
main()