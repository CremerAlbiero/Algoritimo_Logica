degrau = float(input("Digite a altura do degrau em cm: "))
distancia = float(input("Insira a altura que deseja alcançar em metros com a escada: "))

if degrau and distancia <= 0:
    print("O valor não pode ser menor que zero.")

else:
    qtde_degraus = (distancia * 100) / degrau
    print(f"A quantidade necessária será de {qtde_degraus} degraus.")

#Cada degrau de uma escada tem Xcm de altura. Receba a altura de cada degrau em cm e a altura que o usuário deseja alcançar subindo a escada (em metros).
# Faça as conversões, calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.