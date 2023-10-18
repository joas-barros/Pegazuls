def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def imprimirsequencia(n):
    for i in range(1, n + 1):
        print(fibonacci(i), end=" ")


if __name__ == '__main__':
    print("Os primeiros 20 elementos da sequencia de fibonacci são: ")
    imprimirsequencia(20)
