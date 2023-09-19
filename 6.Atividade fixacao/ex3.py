litros_tinta = int(input("Litros de tinta da sua lata: "))
largura_aposento = float(input("Largura do aposento em metros: "))
comprimento_aposento = float(input("Comprimento do aposento em metro: "))

altura_pe_direito = 2.80
largura_porta = 0.80
altura_porta = 2.10

area_paredes = 2 * (largura_aposento + comprimento_aposento) * altura_pe_direito - largura_porta * altura_porta

litros_necessarios = area_paredes / 3

latas_necessarias = litros_necessarios / litros_tinta

print(f"Serão necessárias {latas_necessarias:.2f} latas de tinta.")
















#easter-egg
HelloWorld_latas = 12

if latas_necessarias >= HelloWorld_latas:
    print("O que acha de escrever um belo Hello World no seu aposento?")