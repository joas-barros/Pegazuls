def palindromo(numero):
    str_numero = str(numero)  # transformando o número em string
    # [::-1] inverte um array em python, como uma string é considerada uma tupla, ela é invertida
    return str_numero == str_numero[::-1]  # Verifica se o número é igual ao seu inverso


maior = 0  # Declaramos a variavel maior

for num1 in range(100, 1000):  # Itera todos os numeros de 3 digitos (100 a 999)
    for num2 in range(100, 1000):  # Idem ao anterior
        produto = num1 * num2  # Realizamos o produtos de ambos
        # Verificamos se o produto é um palindromo e se ele é maior que o valor da variavel "maior"
        if palindromo(produto) and produto > maior:
            # Caso a condição seja verdadeira, a variavel maior recebe o produto
            maior = produto

# Imprimos o resultado final: 906609
print(f"o maior número palíndromo que é o produto de dois números de 3 dígitos é {maior}")
