def fibonacci(n):  # Retorna o numero da sequencia de fibonacci na posição n
    if n == 1 or n == 2:  # Os dois primeiros termos da sequencia são iguais a 1
        return 1
    else:
        # Caso não seja os primeiros termos, a função irá retornar a si mesmo para somar os dois termos anteriores
        # até chegar nos dois primeiros termos que já estão definidos
        # essa tecnica é chamada de recursão
        return fibonacci(n - 1) + fibonacci(n - 2)


# Imprime os n primeiro termos da sequencia de fibonacci
def imprimirsequencia(n):
    for i in range(1, n + 1):  # n + 1 pois o range só vai até o penultimo elemento
        print(fibonacci(i), end=" ")  # (end =" ") para manter na linha a cada iteração


if __name__ == '__main__':
    # Chamamos a função imprimirsequencia() que por si chama a função fibonacci para imprimir os 20 primeiros elementos
    print("Os primeiros 20 elementos da sequencia de fibonacci são: ")
    imprimirsequencia(20)
