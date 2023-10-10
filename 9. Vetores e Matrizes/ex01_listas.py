lista = []
for i in range(10):
    lista.append(int(input(f"Digite o número {i + 1}: ")))

#Slice. Sem alterar a lista.
#: início :fim -1(do último pra trás.)
for i in lista[::-1]:
    print(i, end=" ")
    
print(f"\n{lista}")

