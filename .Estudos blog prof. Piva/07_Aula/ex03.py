soma_peso = 0
soma_altura = 0
max_imc = 0
min_imc = 0

for i in range (1, 6):
    peso = float(input(f"Digite o peso da pessoa {i}(KG): "))
    altura = float(input(f"Digite a altura da pessoa {i}: "))
    soma_peso += peso
    soma_altura += altura
    imc = peso / (altura * altura)

    if imc > max_imc:
        max_imc = int(imc)
    
    else:
        min_imc = int(imc)


media1 = soma_peso / 5
media2 = soma_altura / 5

print(f"A média de peso corporal foi: {media1}\nA média de altura foi: {media2}")
print(f"O menor IMC: {min_imc}. Maior IMC: {max_imc}")