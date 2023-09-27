#encontrar 3 numeros na mesma condição.

for n1 in range(-1, 101):
      for n2 in range(-1, 101):
           for n3 in range(-1, 101):
            if n1 * n2 * n3 == n1 + n2 + n3:
                  print(f" {n1} // {n2} // {n3} ")

#Ou seja, [1, 2, 3] ou [-1, 1, 0]