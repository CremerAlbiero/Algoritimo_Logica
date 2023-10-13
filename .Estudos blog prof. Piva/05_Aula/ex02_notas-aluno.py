nota1 = float(input("Digite nota1: "))
nota2 = float(input("Digite nota2: "))
nota3 = float(input("Digite nota3: "))
media = (nota1 + nota2 + nota3) / 3
exame = 0

if media >= 7:
    print("O aluno está aprovado")

elif media >= 3:
    print(f"Você precisa realizar um tirar no mínimo {12 - media} no exame.")
    exame = float(input("Digite a nota do seu exame: "))
    media = (media + exame) / 2
    
    if media >= 6:
        print(f"Você foi aprovado. Sua média final: {media}")
    else:
        print("Reprovado")

else:
    print("o aluno está reprovado.")