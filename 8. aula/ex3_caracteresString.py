while True:
    valor = input("Digite os numeros: ")
    if valor.isnumeric() and len(valor) == 92:
        break
    if len(valor) != 9:
        print("O valor deve ter exatos 9 digitos.")
    else:
        print("Digite apenas números.")
    

novo_valor = valor[0] + "." + valor[1:4] + "," + valor[7:9]
print(novo_valor)


#como fazer funcionar para qualquer digito?