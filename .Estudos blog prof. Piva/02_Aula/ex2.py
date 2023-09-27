#encontrar dois numeros em que o resultado será o mesmo na soma ou multiplicação.

for n1 in range(0, 10):
        for n2 in range (0, 10):
            if n1 * n2 == n1 + n2:
                 print(f"Os números {n1} e {n2}, o resultado entre sua multiplicação ou soma será o mesmo.")

#resultado: 0 e 0; 2 e 2.