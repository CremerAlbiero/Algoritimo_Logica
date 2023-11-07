def volume_raio(r_esfera):
    '''Função que calcula o volume de uma esfera com base no valor de raio fornecido.'''
    from math import pi
    vol = (4/3) * pi * (r_esfera**3)
    return vol
    
r_esfera = float(input("Digite o raio da esfera: "))
retorno = volume_raio(r_esfera)
print(f"O volume da esfera é: {retorno}")