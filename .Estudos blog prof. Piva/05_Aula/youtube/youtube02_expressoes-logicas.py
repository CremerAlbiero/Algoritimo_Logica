#expressoes lógicas

x = 3
y = 5

z = x > y #z >>> False
r = y >= x #r >>> True

'''
Operadores Relacionais:
==  Igual      a==b (a é igual a b?).
!=  Diferente
>   Maior que
<   Menor que
>=  Maior ou igual que
<=  Menor ou igual que

Apenas "=" é utilizado para atribuir valor.
'''

'''
Operadores Lógicos:
and  E   lógico (Realiza op e o resultado é True se ambos forem VERDADEIROS)
or   OU  lógico (Realiza op e o resultado é True se pelo menos um for VERDADEIRO)
not  NÃO lógico (Inverte o estado de um operando)
'''
a = 4
b = 2
not(b==a)         #True (B NÃO é igual a a?)
b==a              #False
b >= 3 or a >= 3  #True
not(b>=3 or a>=3) #False

'''
Prioridade em Python:
()             Parênteses
**             Exponente
+x, -x         Soma ou subtração unária(definição do sinal)
*,/,//,%       Multiplicação, Divisão, Div Inteira e Módulo
+, -           Adição e Subtração
==, !=, >, <   Operadores de Comparação
not            Não lógico
and            E lógico
or             OU lógico

Em uma expressão com todos na mesma linha, essa é a ordem de prioridades em Python.
 '''