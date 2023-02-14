def aforro(capi ,prazo, ta, pc):
    print(" mes |cap. acum.")
    print("-----|---------")
    mes = 0
    capital = capi
    tpr = ta/1200 * pc
    juros = capi * tpr
    print("{:>5}|{:>8s}".format(mes, "{:.2f}".format(capital)))
    for i in range(pc):
        mes += pc
        if mes <= prazo:
            capital += juros
            juros = capital * tpr
            print("{:>5}|{:>8s}".format(mes, "{:.2f}".format(capital)))
    return capital

def main():
    ci = float(input("Capital Inicial:"))
    pt = int(input("Prazo Total (meses):"))
    ta = float(input("Taxa anual líquido (%):"))
    pp = int(input("Periodo de pagamento de juros (meses):"))
    print()
    lucro = aforro(ci, pt, ta, pp) - ci
    print("O lucro obtido no final do periodo é:", "{:.2f}".format(lucro))

if __name__ == "__main__":
    main()