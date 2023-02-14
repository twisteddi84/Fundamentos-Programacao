s=float(input("Introduza os segundos :"))
m = s//60
s2 = (s%60)
h=m//60
m2=m%60
print("{:.0f}:{:.0f}:{:.0f}".format(h, m2, s2))
