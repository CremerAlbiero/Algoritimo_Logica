'''
Metodos:

x in s → True se o elemento x pertence a s
s.add(x) → Inclui o elemento x em s
s.copy() → Retorna uma cópia de s
s.union(r) → Retorna a união entre s e r
s.intersection(r) → Retorna a interseção entre s e r
s.difference(r) → Retorna a diferença entre s e r
list(s) → Retorna os elementos de s numa lista
tuple(s) → Retorna os elementos de s numa tupla
'''
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

# converter para set
a, b = set(a), set(b)

a.union(b)
a.intersection(b)