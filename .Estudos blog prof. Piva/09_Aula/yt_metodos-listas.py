#append()   insere um elemento no final da lista. Modifica a original.
cidades = ['Sorocaba', 'São Paulo', 'Rio de Janeiro', 'New York']
cidades.append('Oslo')

#count()    retorna a qtde de vezes que um item ocorre dentro de uma lista.
cidades.count('São Paulo')    #1
cidades.count('Itu')          #0

#insert()   insere um elemento em determinada posição, deslocando os elementos para a direita.
cidades.insert(2, 'Itu')
print(cidades)

#index()   busca um item na lista e retorna sua posição, caso houver mais de uma, retorna a primeira.
cidades.index('São Paulo')    #1  (se n encontrar, apresenta erro.)

#remove()  remove um determinado elemento (se n encontrar, retorna erro.)
cidades.remove('Itu')

#sort()  irá odernar e MODIFICAR a lista (diferente de sorted.) - ordem alfabética ou numérica.
cidades.sort()

#reverse() inverte a ordem dos elementos. ordem decrescente.
cidades.reverse()

#pop(index) remove um determinado item de uma lista com base no índice. 
#pop()        se não definir o index, ele retira o último da lista.
cidades.pop()
cidades.pop(2)
print(cidades)