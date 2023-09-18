dia = int(input("Entre com o numero do dia: "))


match dia:

    case 1:
        nome = "Domingo"

    case 2:
        nome = "Segunda-Feira"

    case 3:
        nome = "Terça-Feira"

    case 4:
        nome = "Quarta-Feira"

    case 5:
        nome = "Quinta-Feira"

    case 6:
        nome = "Setoou"

    case 7:
        nome = "Sábado"
    
    case _:
        nome = "Dia Inválido. Digite novamente de 1 a 7"

print(nome)