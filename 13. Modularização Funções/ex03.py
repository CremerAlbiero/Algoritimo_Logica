def is_prime(n):
    primo = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                primo = False
                return False
        if primo:
            return True
        else:
            return False
    else:
        return False

result = is_prime(1)
print(result)