def tax(r):
    if r<=1000:
        r = 0.1*r
    elif 1000<r<=2000:
        r =0.2*r-100
    else:
        r =0.3*r-300
    return r

def main():
    n1 = float(input("Number:"))
    n1 = tax(n1)
    print(n1)

main()