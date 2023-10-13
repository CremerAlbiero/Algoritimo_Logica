n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

print("\nO que você deseja saber?\n1. Média entre os números digitados\n2. Diferença do maior pelo menor\n3. Produto entre os números digitados\n4. Divisão do primeiro pelo segundo")
opcao = input("\nDigite apenas o número selecionado (1, 2, 3 ou 4): ")

media = (n1 + n2) / 2
if n1 > n2:
    diferenca = n1 - n2
else:
    diferenca = n2 - n1

produto = n1 * n2
divisao = n1 / n2


if opcao == "1":
    print(f"A média entre os dois números é: {media}")

elif opcao == "2":
    print(f"A diferença entre eles é {diferenca}")

elif opcao == "3":
    print(f"O produto dos números é: {produto}")

elif opcao == "4":
    print(f"A divisão entre os números é: {divisao}")