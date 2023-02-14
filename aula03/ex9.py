def conv(s):
    min = s//60
    sec = s%60
    hora = min//60
    min = min%60
    return hora,min,sec

def main():
    segundos = float(input("Segundos :"))
    s=conv(segundos)
    print(s)

main()