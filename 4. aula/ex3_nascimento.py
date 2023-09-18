ano = 2023
nascimento = int(input("Data de Nascimento: "))
idade = ano - nascimento
meses = idade * 12
dias = meses * 30
semanas = dias / 7
    
print("A sua idade é:", idade,".","Vc tem:", meses,"meses")