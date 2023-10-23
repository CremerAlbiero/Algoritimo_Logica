num_primos = []
num = 101

while len(num_primos) < 10:
    if num > 1:
        primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            num_primos.append(num)
    num += 1

print(num_primos)