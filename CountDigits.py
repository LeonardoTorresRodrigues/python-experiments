def count_digits(n, d):
    n_str = str(n)
    count = 0
    for digit in n_str:
        if digit == str(d):
            count += 1
    return count


n = int(input("Digite o valor de n (n > 0): "))
d = int(input("Digite o valor de d (0<=d<=9): "))

occurrences = count_digits(n, d)
print(f"O dígito {d} ocorre {occurrences} vezes em {n}")
