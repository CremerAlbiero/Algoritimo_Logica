compra = float(input("Digite o valor da sua compra: "))

if compra <= 1000:
 desconto =   compra-(compra*1.10)
 
elif compra >= 5000:
    desconto = compra-(compra*1.30)
    
else:
    desconto = compra-(compra*1.20)
 

print(f"O desconto total foi de: {desconto}.", f"Valor final com desconto R$ {compra -- desconto}")
