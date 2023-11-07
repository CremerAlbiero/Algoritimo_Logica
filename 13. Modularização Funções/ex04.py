def bissexto(ano):
  if ano % 4 == 0:
    if ano % 100 == 0:
      if ano % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

ano = int(input("Digite um ano e verifique se é bissexto\n"))
result = bissexto(ano)

if result:
    print(f"O ano {ano} é um ano bissexto")
else:
    print(f"O ano {ano} não é bissexto.")