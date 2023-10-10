lista = list(range(1,8))
for i in lista:
    print(i, end=" / ")
    
#list.reverse()  reverta o nome da lista
lista.reverse()
print(lista)

#listsort() ordena a lista. 
# Ex: lista.sort(reverse=False) ou lista.sort(reverse=True).
lista.sort(reverse=False)
print(lista)

#métodos de classe list (funções)
#ex: atribuir funcao para ordernar valores com base no comprimento.
lista2 = ['abc', 'de', 'fghi']
lista2.sort(key=len)
print(lista2)