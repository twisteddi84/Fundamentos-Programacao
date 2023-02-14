def p(x):
	return x**2+2*x+3

def main():
	print("p(x)=x^2+2x+3")
	resultado = p(0)
	print("Resultado de p(0) é {}.".format(resultado))
	resultado = p(1)
	print("Resultado de p(1) é {}.".format(resultado))
	resultado = p(2)
	print("Resultado de p(2) é {}.".format(resultado))
	resultado = p(p(1))
	print("Resultado de p(p(1)) é {}.".format(resultado))

main()
