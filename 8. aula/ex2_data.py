#Faça um algoritmo que solicite uma data no formato de uma string – dd/mm/aaaa. Mostre essa data no formato AAAAMMDD

data = input("Digite a data como dia/mês/ano: ")
dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

print(f"{ano}{dia}{mes}")

