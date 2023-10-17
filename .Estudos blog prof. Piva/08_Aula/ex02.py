data = input("Digite a data atual DD/MM/AAAA (sem pontuações): ")

dd = int(data[0:2])
mm = int(data[2:4])
aa = int(data[4:8])

#exibir no formato AAAAMMDD
print(aa,mm,dd)