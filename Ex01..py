def eprimo(n):
    divisor = n  # Criando o valor que será atualizado no laço de repetição
    contador = 0  # Conta quantos números são multiplos de n
    while divisor >= 1:
        if n % divisor == 0:  # verifica se o numero é um multiplo
            contador += 1  # Caso seja ele é contabilizado
        divisor -= 1  # Atualizamos o proximo valor a ser verificado até chega em 1

    # Caso o número possua 2 ou menos multiplos ele será considerado primo
    if contador <= 2:
        return True
    else:
        return False


# A seguinte condicional faz com que essa parte do codigo seja executada somente quando executamos o arquivo
# Sendo assim ele não é executado quando importamos como módulo
if __name__ == '__main__':
    numero = int(input("Digite um número inteiro: "))
    # Verifica se o numero informado pelo usuario é primo ou não chamando a função que criamos
    # Imprime a respectiva mensagem de acordo com o valor lógico da condição
    if eprimo(numero):
        print(f"{numero} é primo")
    else:
        print(f"{numero} não é primo")
