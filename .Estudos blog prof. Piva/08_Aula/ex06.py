palavra = input("Digite uma palavra: ")
palavra = palavra.lower()

if palavra[::-1] == palavra:
    print("É um palíndromo! A palavra é igual de trás para frente!")
else:
    print("Não é um palíndromo.")