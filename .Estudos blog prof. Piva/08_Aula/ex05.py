frase = input("Escreva uma frase: ")
frase = frase.split()
palavras = len(frase)
print(f"O total de palavras da frase é: {palavras}")

#retirar os espaços por meio do split, separando-os em uma lista p/ evitar erros de não contar palavras com pontuação e vírgulas ao lado, assim como a palavra final.