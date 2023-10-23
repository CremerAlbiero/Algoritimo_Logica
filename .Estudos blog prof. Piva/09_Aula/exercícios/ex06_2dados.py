from random import randint
soma_dados = []
for i in range(1, 30001):
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma_dados.append(dado1 + dado2)

soma_2 = soma_dados.count(2) 
soma_3 = soma_dados.count(3) 
soma_4 = soma_dados.count(4) 
soma_5 = soma_dados.count(5) 
soma_6 = soma_dados.count(6) 
soma_7 = soma_dados.count(7) 
soma_8 = soma_dados.count(8) 
soma_9 = soma_dados.count(9)  
soma_10 = soma_dados.count(10)  
soma_11 = soma_dados.count(11) 
soma_12 = soma_dados.count(12)

if soma_7 / 30000 >= 1/6:
    porcentagem_7 = True
else:
    porcentagem_7 = False

print(f"Considerando a soma dos dois dados 30.000 vezes, segue quantidade:")
print(f"2: {soma_2}\n3: {soma_3}\n4: {soma_4}\n5: {soma_5}\n6: {soma_6}\n7: {soma_7}\n8: {soma_8}\n9: {soma_9}\n10: {soma_10}\n11: {soma_11}\n12: {soma_12}")

if porcentagem_7:
    print(f"A soma dos dados com total 7 foi maior ao total de jogadas.")
else:
    print("A soma dos dados com total 7 foi menor que 1/6 do total de jogadas.")

# Faça um algoritmo que simule a jogada de dois dados de 6 faces. O programa deve usar randintpara rolar o primeiro dado e deve usar randint novamente para rolar o segundo dado. 
# A soma das duas faces deve ser calculada. Assim: a soma variará de 2 a 12
# O programa deve rolar 30.000 vezes e mostrar a frequência com que a soma (de 2 a 12) aparecem. Verifique se o valor 7 corresponde a 1/6 das jogadas