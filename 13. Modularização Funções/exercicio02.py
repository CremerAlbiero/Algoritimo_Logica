def formatar_nome(primeiro_nome, segundo_nome):
    primeiro_n = primeiro_nome.title()
    segundo_n = segundo_nome.title()
    
    return f"{primeiro_n} {segundo_n}"

# O return guarda o valor e depois esse valor está sendo guardado na variável.
print(formatar_nome("adam", "back"))