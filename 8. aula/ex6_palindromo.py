palavra = input("Digite uma palavra: ")

if palavra[::-1].lower() == palavra.lower():
    print(f"{palavra} é uma palavra palíndroma!")
else:
    print(f"{palavra} não é uma palavra palíndroma.")