def é_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def n_primos(n):
    if n < 2:
        return 0

    count_primos = 0
    for i in range(2, n + 1):
        if é_primo(i):
            count_primos += 1
    return count_primos


n = int(input("Digite um número maior ou ingual a 2: "))
total_primos = n_primos(n)
print(total_primos)
