ctp = float(input("Introduza a nota da CTP:"))
cp = float(input("Introduza a nota da CP:"))
notafinal = int(ctp*0.36 + cp*0.64)

if ctp<6.5 or cp<6.5 :
	print("Nota final: código 66")
elif notafinal<10 :
	atpr = float(input("Introduza a nota da ATPR :"))
	apr = float(input("Introduza a nota da APR :"))
	notafinal = int(max(atpr,ctp)*0.36+max(cp,apr)*0.64)
	print("Nota final: {}.".format(notafinal))
	
else:
	print("Nota final: {}.".format(notafinal))	
