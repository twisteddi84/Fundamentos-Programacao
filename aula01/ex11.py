from math import ceil
nome = input("Qual é o seu nome?")
apelido = input("Qual é o seu apelido?")
sal_men= float(input("Quanto recebe de salário mensal?"))
sub_ali=float(input("Quanto recebe de subsídio de alimentação?"))
sal_an = sal_men*12
alimentaçao_ano = sub_ali*12
total = sal_an + alimentaçao_ano
print("O/A {} {} recebe:\n   {:.2f} euros de salário ao fim de 1 ano;\n   {:.2f} euros de subsídio de alimentação ao fim de 1 ano;\n   {:.2f} euros no total ao fim de 1 ano;".format(nome,apelido,ceil(sal_an*100)/100,ceil(alimentaçao_ano*100)/100,ceil(total*100)/100))