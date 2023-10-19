def palindromo(numero):
    str_numero = str(numero)
    return str_numero == str_numero[::-1]


maior = 0

for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        produto = num1 * num2
        if palindromo(produto) and produto > maior:
            maior = produto

print(maior)
