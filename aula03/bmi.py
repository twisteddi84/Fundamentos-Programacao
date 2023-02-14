def bodyMassIndex(height, weight):
    return weight/(height**2)

def bmiCategory(imc):
	if imc<18.5:
		return ("underweight")
	elif 18.5<=imc<25:
		return("normal weight")
	elif 25<=imc<30:
		return("overweight")
	elif 30<imc:
		return("obesity")



def main():
    print("Índice de Massa Corporal")
    
    altura = float(input("Altura (m)? "))
    if altura < 0:
        print("ERRO: altura inválida!")
        exit(1)

    peso = float(input("Peso (kg)? "))
    if peso < 0:
        print("ERRO: peso inválido!")
        exit(1)

    
    imc = bodyMassIndex(altura, peso)
    cat = bmiCategory(imc)

    print("BMI:", imc, "kg/m2")
    print("BMI category:", cat)

main()

