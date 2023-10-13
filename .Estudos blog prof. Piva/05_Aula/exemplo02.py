alfa = True
beta = False
x = 2
y = 0

'''
cada uma das expressoes são chamadas expressoes relacionais.
and or são conectores. Ligam as expressoes relacionais.
True/False são constantes lógicas.
alfa e beta, que são comparadas com as constantes, são variáveis lógicas.

"==" é um Operador Relacional, indica uma comparação.
'''
#Estrutura Condicional Simples: comando só é executado se a condição for verdadeira:
if x == 0:
    print("x = 0")

#Estrutura Condicional Composta: 
#conjunto de comandos que devem ser rexecutados em uma ordem específica (Ifs/ If Else).
if alfa == True  and beta == False and (x == 0 or y == 0):
    print("Expressao verdadeira")
else:
    print("Expressao falsa")



