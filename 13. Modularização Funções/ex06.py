def hora_segundos(h, m, s):
    h *= 3600
    m *= 60
    total_segundos = s + h + m
    return total_segundos

h = int(input("Digite a hora: "))
m = int(input("Digite os minutos: "))
s = int(input("Digite os segundos: "))

conversao = hora_segundos(h, m, s)

print(f"hora digitada: {h}:{m}:{s}")
print(f"O total de segundos é {conversao}.")