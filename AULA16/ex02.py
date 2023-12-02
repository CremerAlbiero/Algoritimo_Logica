def verifica_primo(n):
    primo = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                primo = False
        if primo:
            return True
        else:
            return False
    else:
        return False

print(verifica_primo(28))


def qtd_primo(n):
    t_primos = 0
    for i in range(0, n + 1):
        if verifica_primo(i): 
            t_primos += 1
    return t_primos

print(qtd_primo(28))


# consegui com apenas um range chamando a função "verifica_primo."
funcao = 28 * 2 + 5
l_primos = []
for i in range(2, funcao + 1):
    if verifica_primo(i):
        l_primos.append(i)

# lista completa:
print(l_primos)

# para somar a lista, utilizei sum() e guardei o valor em uma variável
soma = sum(l_primos)
print(soma)