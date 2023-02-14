def countsDigit(n):
    lst=[]
    for i in n:
        if i.isdigit():
            lst.append(i)
        else:
            True
    return len(lst)
def main():
    n = input("Frase:")
    print("Contém {} digitos.".format(countsDigit(n)))

main()