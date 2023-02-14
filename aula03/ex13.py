def mdc(a,b):
    res = a%b
    if res == 0:
        return b
    else:
        return mdc(b,res)

#MAIN FUNCTION
def main():
    x1 = int(input("Um número inteiro:"))
    x2 = int(input("Outro número inteiro:"))
    print("O máximo divisor comun entre {} e {} é {}.".format(x1,x2,mdc(x1,x2)))

main()