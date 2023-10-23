#Indexação e fatiamento de listas
lista1 = [1, 3, 5, 7]
frase = "Um texto qualquer"
lista_caracteres = list(frase)

lista1[0]

#índice negativo vai de trás para frente.
lista1[-1]

#utilizando passo [inicio:fim:passo]:
lista_caracteres[::-2]   #do início ao fim, pulando os elementos de 2 em 2 (de trás pra frente).
print(lista_caracteres[::-1])  #lista de trás pra frente.