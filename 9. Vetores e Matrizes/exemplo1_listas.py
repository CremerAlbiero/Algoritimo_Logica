lista = [1, 3.5, 'a', [3, 56, "b"]]

lista[1] #elemento 1 (começa com 0)

lista[3] #[3, 56, 'b']

lista[2] = "Ana"

lista[0] = 'a'
#você pode alterar elementos dentro da lista. Agora lista possui "Ana" no lugar de "a".

lista2 = [lista]
lista2[1][3][2]

#concatenação
lista3 = lista + lista2

lista[0] = lista2[0] + lista[0]  # cada uma possui o valor 'a' na posição 0
lista[0] # 'aa"


#remover um elemento da lista
del lista[1]

#inicializar listas adicionar valores: .append
#adiciona 1 elemento por vez.
lista = []
lista[0] = 1
# Traceback (most recent call last)

lista.append(1)
# >>> lista [1]. Foi adc um valor.

#Len, min e max






