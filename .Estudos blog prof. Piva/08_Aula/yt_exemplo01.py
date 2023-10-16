frase = '''utilizando três aspsas,
você pode teclar diretamente o espaço e gerar "quebra" de linhas.'''

print(frase)

#posição caracter (utilizando slice):
print(frase[0])

#pega o primeiro valor da string / 2º: traz o limite do valor (n-1) / 3º: tamanho do passo (pula posições)
print(frase[0:10])

#3º parâmetro: passo (mostra um caracter, pula outro):
print(frase[0:10:2])


#valores negativos:
print(frase[::-1]) #:inicie desde o começo, : vá até o final, -1: de traz pra frente.