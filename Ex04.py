def fatorial(n):
    f = 1  # começa no 1 pois é o elemnto neutro da multiplicação
    for i in range(1, n + 1):  # n + 1 pois o range só vai até o penultimo elemento
        f *= i  # multiplica a variavel f n vezes
    return f


if __name__ == '__main__':
    numero = int(input("Digite um número inteiro positivo: "))
    # Verificando o sinal do numero (Nunca confie no usuario)
    if numero < 0:
        print("Não podemos calcular fatorial de número negativo!!!")
    else:
        # Caso seja positivo, chamamos a função criada
        print(f"{numero}! = {fatorial(numero)}")
