ano_atual = input("Digite o ano atual: ")
ano_nascimento = input("Digite seu ano de nascimento: ")

if len(ano_nascimento) and len(ano_atual) == 4:
    ano_nascimento = int(ano_nascimento)
    ano_atual = int(ano_atual)
    idade = ano_atual - ano_nascimento
    votar = idade >= 16
    dirigir = idade >= 18

    if votar:
        print("você já pode votar.")

    elif dirigir:
        print("você já pode tirar sua CNH e votar.")
    
    else:
        print("Você ainda não possui idade suficiente.")

else:
    print("Erro. Digite o ano apenas com 4 números.")