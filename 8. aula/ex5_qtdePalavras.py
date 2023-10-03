#determinar quantas palavras específicas existem em uma frase.
phrase = input("Digite uma frase sobre amor: ")

for words in phrase:
    if phrase == "amor":
        phrase += 1
 
total_palavra = phrase.count("amor")


print(f"O total de palavras amor digitas é {total_palavra}")