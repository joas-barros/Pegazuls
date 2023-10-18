def fatorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


if __name__ == '__main__':
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        print("Não podemos calcular fatorial de número negativo!!!")
    else:
        print(f"{numero}! = {fatorial(numero)}")
