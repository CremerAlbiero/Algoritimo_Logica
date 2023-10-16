soma = 0
total_m = 0
total_n = 0

while True:
    m = int(input(f"Digite o valor de m (sair: -1): "))
    n = int(input(f"Digite o valor de n (sair: -1): "))

    if m < n:
         print("Erro. M deve ser maior que N.")
         break
    
    elif m % 2 != 0 or n % 2 != 0:
        print("Erro. Valor deve ser par.")
        break

    else:
        soma += 2
        total_m += m
        total_n += n
print(f"A soma total de m: {total_m}. e o total de n foi: {total_n}.\nNúmeros válidos digitados: {soma}")
