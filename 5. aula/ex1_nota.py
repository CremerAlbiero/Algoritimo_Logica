nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
nota3 = float(input("nota 2: "))
media = (nota1 + nota2 + nota3) / 3
nota_exame = 0

if media < 3:
    resultado = "Reprovado"

else:
    if media < 7:
        resultado = "Exame"
        nota_exame = 12 - media
    else:
        resultado = "Aprovado"

print(f"Media {media:5.2f} - {resultado}!")
if nota_exame != 0:
    print(f"Tem que tirar no minimo {nota_exame:5.2f}")