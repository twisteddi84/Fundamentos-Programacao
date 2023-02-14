def iseven():
    n=0
    while n<101:
        mult=0
        for count in range(2,n):
            if (n % count == 0):
                mult += 1

        if(mult==0):
            print("{}: True".format(n))
        else:
            print("{}: False".format(n))
        n +=1
def main():
    print("NÚMEROS PRIMOS")
    iseven()

main()