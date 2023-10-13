preco = float(input("Digite o preço do produto: "))
regiao = input("Digite o codigo da sua região: ")
imposto = float(0)

if regiao == "1":
    imposto = 0.11
    nome_regiao = "Sul"

elif regiao == "2":
    imposto = 0.13
    nome_regiao = "Norte"

elif regiao == "3":
    imposto = 0.09
    nome_regiao = "Nordeste"

elif regiao == "4":
    imposto = 0.12
    nome_regiao = "Centro-Oeste"

elif regiao == "5":
    imposto = 0.18
    nome_regiao = "Sudeste"

    imposto_produto = imposto_produto = (imposto * preco) + preco
    print(f"O imposto da região {nome_regiao} é de {imposto * 100}%. Preço com imposto: R${imposto_produto}")

else:
    print("Cod Inválido")