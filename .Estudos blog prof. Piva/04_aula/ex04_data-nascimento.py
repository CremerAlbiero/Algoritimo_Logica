#algoritmo que receba a data de nascimento de uma pessoa e a data atual e mostre sua idade em anos, meses, semanas e dia.

from datetime import datetime
data_nascimento = input("Digite a data de nascimento (YYYYMMDD): ")

data_nascimento = datetime.strptime(data_nascimento, "%Y%m%d")

data_atual = datetime.now()

diferenca = data_atual - data_nascimento

idade_anos = diferenca.days // 365
idade_meses = (diferenca.days % 365) // 30
idade_semanas = (diferenca.days % 365) // 7
idade_dias = diferenca.days

print(f"Sua Idade é: {idade_anos}\nMeses: {idade_meses}\nSemanas: {idade_semanas}\nDias: {idade_dias}")