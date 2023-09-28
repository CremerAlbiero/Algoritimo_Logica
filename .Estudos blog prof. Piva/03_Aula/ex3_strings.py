#barra invertida

# \n: new line (quebra a linha)
print("Linha1\nLinha2")

# \t é o mesmo que tab
print("Olá,\t!")

#  \b é o mesmo que backspace (deleta o útlimo caractere antes de \b e substitui pelo caractere na frente)
print("Palavr1\ba") # "Palavra"

# \\ é o mesmo que \
print("25 \\ 45")   # 25 \ 45


# \x41 é o mesmo que o caractere cujo código hexadecimal é 41 
print("\x4F\x4C\x41") #OLA


#m é possível escrever constantes string em várias linhas incluindo as quebras de linha usando três aspas como delimitadores
print("""
      um tigre
      dois tigres
      tres tigres
      """)

#índices string (ex: 1: primeiro valor/ -1 ultimo valor)
ab = str('Computer')
print(ab[0])
print(ab[-1])


#slices (fatias). Notação para separar trechos de uma string:
slice = "abcde"
print(slice[0:2]) #ab
print(slice[-1:]) #e
print(slice[:-1]) #abcd

