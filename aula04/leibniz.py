def leibniz(n):
    t=0
    r2 = 0
    while t <= n:
        r = ((-1)**t)/((2*t)+1)
        r2 = r2 + r
        t +=1
    return r2
def main():
    n = int(input("Introduza um número:"))
    n=leibniz(n)
    print(n)

main()