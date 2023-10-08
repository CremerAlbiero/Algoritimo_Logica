hora = float(input("Insira a hora atual: "))
minutos = (int(hora) *60) + ((hora - int(hora)) * 100)
print(f"total de minutos: {minutos}")

# receba uma hora formada por hora e minutos (um número real), calcule e mostre a hora digitada apenas em minutos. 
# Lembre-se de que: Para quatro e meia deve-se digitar: 4,30;  Os minutos vão de 0 a 60.