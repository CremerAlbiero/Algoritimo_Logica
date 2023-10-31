# lista é mutável. tuplas é imutável.
tupla = (1, 2, 3, 4, 5)
tupla2 = (2, 3, 4)

# foi criada para fazer manipilações de dados para que você não altere o valor original.

#métodos tuplas:
tupla.count(5)  #conta quantas vezes ocorre determinado item.
tupla.index(4)  #busca um item em uma tupla e retorna sua posição. Se tiver mais d eum aocorrência do item, retorna a primeira.
tupla[1:3]      #retorna o valor na posição de memória


#concatenação:
tupla3 = tupla + tupla2
print(tupla3)