#determinar qts vogais existem dentro de uma frase (que deve ser recebida do usuário).

frase = input("Digite uma frase: ")
qtde = 0

for letra in frase:
    if letra.lower() in 'aeiou':
        qtde = qtde + 1
        
print(f"A frase possui {qtde} vogais.")