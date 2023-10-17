frase = input("Escreva uma frase: ")
frase.lower()
cont = frase.count('a')
cont += frase.count('e')
cont += frase.count('i')
cont += frase.count('o')
cont += frase.count('u')
print(f"A frase possui {cont} vogais.")

#utilizando algumas built-in functions desta aula.