#str-strip: retira todo espaço em branco deixado pelo usuário;
#str-title: coloca a primeira letra da string em maiúsculo;
#str-split(delimit): separa uma string conforme um delimitador. Inverso de join.
#str-join(sequence): Junta cada item da string com um delimitador especificado. Inverso de split.

texto1 = input("Digite seu texto: ")
texto2 =  input("Digite seu 2º texto: ")

print(texto1.split(), texto2.split())