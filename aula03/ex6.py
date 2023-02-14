def inter(x1,y1,x2,y2):
    if y1>x2 and x1<y2 or x1<y2 and x2<y1 :
        return 0==0
    else:
        return 0==1
    return

def main():
    a1 = float(input("Introduza a1 :"))
    b1 = float(input("Introduza b1 :"))
    a2 = float(input("Introduza a2 :"))
    b2 = float(input("Introduza b2 :"))
    if a1>=b1 or a2>=b2 :
        print("Intervalos inválidos.")
    else :
        resultado = inter(a1,b1,a2,b2)
        print("Os intervalos intersetam-se : {}".format(resultado))

main()