#receber o salário de um funcionário, calcular e mostrar o novo salário com 15,3% de aumento.

salario_anterior = float(input("Digite o seu salário atual para verificar quanto você passará a receber: "))
novo_salario = salario_anterior * 1.153

print(f"Seu salário era R$ {salario_anterior}. Agora com o ajuste de 15,3%, será R$ {novo_salario}")