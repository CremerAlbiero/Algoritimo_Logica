#built-in dict functions
telefones = {"Ana": 17993458329, "Joao": 14886437649, "Pedro": 31697432363, "Maria": 6549344923}
telefones2 = {"Ana": 17993458329, "Joao": 14886437649, "Pedro": 31697432363}

# clear() Remove todos os elementos do dicionários
telefones2.clear()

# fromkeys(lista,valor)   

#get(chave, valor)  obtém o conteúdo da chave.
telefones.get("Maria")

# pop(chave)   remove a chave e seu par correspondente.
telefones.pop("Pedro")
print(telefones)
