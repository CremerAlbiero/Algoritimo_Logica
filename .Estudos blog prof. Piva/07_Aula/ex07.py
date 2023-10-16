n = 10
a = 1
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#atribuição múltipla em python: a, b
#seria necessário uma var receber valor de a; a receber valor de b; b receber <var + a> em loop.