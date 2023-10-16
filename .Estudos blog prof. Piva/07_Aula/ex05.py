tempo = 600

for segundos in range(tempo, -1, -1):
    minutos = segundos // 60
    segundos = segundos % 60
    print(f"{minutos:02d}:{segundos:02d}")
          
print("The end.")

#// realiza a divisão e arredonda o resultado.