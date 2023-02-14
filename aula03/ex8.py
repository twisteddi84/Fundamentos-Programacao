def conv(h, m, s):
    s =(h*60*60)+(m*60)+s
    return s

def main():
    hora = float(input("Hora:"))
    min = float(input("Minutos:"))
    sec = float(input("Segundos:"))
    segundos = conv(hora, min, sec)
    print("{:.0f}h:{:.0f}m:{:.0f}s são precisamente {:.0f} segundos.".format(hora,min,sec, segundos))

main()