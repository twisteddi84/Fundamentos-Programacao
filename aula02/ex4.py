litros = float(input("Quantos litros deseja abastecer ?"))
if litros<=40 :
	preço = litros*1.4
	print("Tem de pagar {:.2f}€.".format(preço))
else:
	preço = (litros*1.4)*0.9
	print("Tem de pagar {:.2f}€.".format(preço))
