#Estrutura condicional If (testar conexões)
'''
if <expressao_logica1>:
    if <expressao_logica2>:
          <comando1>
    else:
          <comando2>

else:
   <comando3>

se a condição1 for verdadeira, e a condição2 for verdadeira = executa comando1.
se a condição 1 for verdadeira, e a condição 2 FALSA = executa comando2.
se a condição1 for FALSA = executa comando 3.
'''

#exemplo ifs alinhados

num = int(input("Digite um número inteiro(negativo ou positivo): "))

if num >= 0:
    if num % 2 == 0:
        print(f"Número {num} é par e positivo.")
    else:
        print(f"Número {num} é ímpar e positivo.")

else:
    if num % 2 == 0:
        print(f"Número {num} é par e negativo.")
    else:
        print(f"Número {num} é ímpar e negativo.")
print("Fim do programa.")