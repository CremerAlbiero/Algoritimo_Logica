for i in range(5):
    if i == 0:
        print('\ni = 0')
        continue
    elif i == 1:
        print('\ni = 1')
        continue
    elif 1 < i < 3:
        print("\nA variável i, é: ", i)
    elif i == 3:
        print('\ni = 3, então: break')
        break   
    else:
        print("\ni > 3, então: ", i)

#break: sai do laço de repetição.
#else: será executado quando a condição do laço for falsa.