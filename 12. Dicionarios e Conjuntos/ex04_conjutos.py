list1, list2 = [], []
for i in range(1, 6):
    elements1 = int(input(f"Digite o numero {i} da primeira lista: "))
    list1.append(elements1)
    
for i in range(1, 6):
    elements2 = int(input(f"Digite o numero {i} da segunda lista: "))
    list2.append(elements2)
    
conjunto = set(list1).union(list2)
print(conjunto)

#imprimir item por item:
for items in conjunto:
    print(items)