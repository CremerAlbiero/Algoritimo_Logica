lista = [1, 2, 9, 3, 4]

#len retorna o número de elementos da lista
print(len(lista))

#min(lista)  retorna o menor/maior elemento da lista.
print("\nmin max:")
min(lista)
max(lista)

#para strings, considera min(): elemento com MENOR caracteres e ordem alfabética.
# max(): considera MAIOR elemento em caracteres e ordem alfabética.
lista2 = ['aa', 'z', 'b','zz' ,'bb', 'a']

print("No caso de caracteres: ")
min(lista2)   #a
max(lista2)  #zz