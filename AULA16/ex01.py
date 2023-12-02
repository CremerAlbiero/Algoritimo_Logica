def pes_cabecas(cabecas, pes):
    t_patos = int(pes / 2)   #pato tem 2 pés
    t_coelhos = int(pes / 4) #coleho tem 4 pés
    return t_patos, t_coelhos

y = 28
teste = pes_cabecas(y * 2 + 5, y* 3 + 7)
print(teste)