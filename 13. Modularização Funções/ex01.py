def par_check(num):
    if num % 2 == 0:
        return True
    return False

result = par_check(3)

if result:
    print("Número par.")
else:
    print("Número ímpar.")