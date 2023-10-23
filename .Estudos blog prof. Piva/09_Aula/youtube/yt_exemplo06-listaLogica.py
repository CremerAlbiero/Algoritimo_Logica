lista_logica = [True, True, False]

any(lista_logica)
all(lista_logica)


#True é considerado "1 ou qualquer n diferente de 0". False é considerado "0".
lista_logica2 = [0, 0, 0, 1, 0]
any(lista_logica2)  #True

lista_logica2[3] = 0
any(lista_logica2)  #False (não há nenhum elemento verdadeiro.)

lista_logica2[3] = 8
any(lista_logica2)  #True


lista_ordenada = [2, 10, 23, 4, 7, 3]
lista_ordenada = sorted(lista_ordenada)    #[2, 3, 4, 7, 10, 23]