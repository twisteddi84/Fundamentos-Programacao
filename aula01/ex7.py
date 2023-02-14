import math
x1=float(input("Introduza o x1:"))
y1=float(input("Introduza o y1:"))
x2=float(input("Introduza o x2:"))
y2=float(input("Introduza o y2:"))

dis = math.sqrt((x2-x1)**2+(y2-y1)**2)

print("A distância entre o ponto ({},{}) e ({},{}) é de {:.2f}.".format(x1,y1,x2,y2,dis))