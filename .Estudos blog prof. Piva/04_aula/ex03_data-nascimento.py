#receba o ano de nascimento de uma pessoa e o ano atual e mostre: idade em anos, meses, dias e semanas.

data_nascimento = input("A data de seu nascimento DD/MM/AAAA (sem pontuações): ")
data = input("Digite a data atual DD/MM/AAAA: ")

dia_nascimento = int(data_nascimento[0:2])
mes_nascimento = int(data_nascimento[2:4])
ano_nascimento = int(data_nascimento[4:8])


dia_atual = int(data[0:2])
mes_atual = int(data[2:4])
ano_atual = int(data[4:8])

match mes_nascimento:
    case 1: 
        mes1 = "janeiro"

    case 2: 
        mes1 = "fevereiro"
        
    case 3: 
        mes1 = "março"

    case 4: 
        mes1 = "abril"

    case 5: 
        mes1 = "maio"

    case 6: 
        mes1 = "junho"

    case 7: 
        mes1 = "julho"

    case 8: 
        mes1 = "agosto"

    case 9: 
        mes1 = "setembro"

    case 10: 
        mes1 = "outubro"

    case 11: 
        mes1 = "novembro"

    case 12: 
        mes1 = "dezembro"

match mes_atual:
    case 1: 
        mes2 = "janeiro"

    case 2: 
        mes2 = "fevereiro"
        
    case 3: 
        mes2 = "março"

    case 4: 
        mes2 = "abril"

    case 5: 
        mes2 = "maio"

    case 6: 
        mes2 = "junho"

    case 7: 
        mes2 = "julho"

    case 8: 
        mes2 = "agosto"

    case 9: 
        mes2 = "setembro"

    case 10: 
        mes2 = "outubro"

    case 11: 
        mes2 = "novembro"

    case 12: 
        mes2 = "dezembro"

print(f"Você nasceu no dia {dia_nascimento} de {mes1} de {ano_nascimento}.")
print(f"\nA data atual é {dia_atual} de {mes2} de {ano_atual}.")

#idades
idade_anos = (ano_atual - ano_nascimento)
if mes_atual < mes_nascimento:
    idade_anos = idade_anos - 1

idade_meses = mes_atual - mes_nascimento
if mes_atual <0:
    idade_meses += 12

idade_dias = dia_atual - dia_nascimento
if idade_dias <0:
    idade_dias +=30
    idade_meses += -1


print(f"\nVocê possui atualmente, {idade_anos} anos, {idade_meses} meses,{idade_dias} dias de vida!")


