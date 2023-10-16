qtde = 0
soma_h = 0
soma_p = 0

while qtde < 10:
    qtde += 1
    h = float(input(f"Digite a altura da pessoa {qtde}: "))
    p = float(input(f"Digite o peso da pessoa {qtde}: "))
    soma_h += h
    soma_p += p

    if qtde == 10:
        media_h = soma_h / qtde
        media_p = soma_p / qtde
        print(f"O número de pessoas foram {qtde}.\nMédia de altura: {media_h}.\nMedia de peso: {media_p}.")
        break