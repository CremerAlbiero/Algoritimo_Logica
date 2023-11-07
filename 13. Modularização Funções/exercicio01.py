def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def divisao(n1, n2):
    return n1 / n2

def multiplicacao(n1, n2):
    return n1 * n2

operacoes_basicas = ["+", "-", "/", "*"]

n1 = int(input("n1: "))
for i in operacoes_basicas:
        print(i)
op = input("Qual operação você deseja fazer?\n")
n2 = int(input("n2: "))


def tipo_op(op):
    if op == "+":
        return soma(n1, n2)
    elif op == "-":
        return subtracao(n1, n2)
    elif op == "/":
        return divisao(n1, n2)
    elif op == "*":
        return multiplicacao(n1, n2)
    else:
       return "Operação Inválida"

resultado = tipo_op(op)

if op in operacoes_basicas:
    print(f"{n1} {op} {n2} = {resultado}")
    
else:
    print("Tipo inválido de operação.")