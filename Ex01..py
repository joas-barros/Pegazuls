def eprimo(n):
    divisor = n
    contador = 0
    # Conta quantos números são multiplos de n
    while divisor >= 1:
        if n % divisor == 0:
            contador += 1
        divisor -= 1

    if contador <= 2:
        return True
    else:
        return False


if __name__ == '__main__':
    numero = int(input("Digite um número inteiro: "))
    if eprimo(numero):
        print(f"{numero} é primo")
    else:
        print(f"{numero} não é primo")
