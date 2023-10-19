i = 1
lista = []
# Adiciona quantos elementos o usuarios quiser na lista
while True:
    num = int(input(f"Digite o {i}º valor da lista: "))
    lista.append(num)
    i += 1  # atualizando o indice

    # .strip() remove possiveis espaços que o usuario digitar
    # .upper() transforma tudo em maiuscula
    # [0] pois só queremos o primeiro caractere da string (S ou N)
    verificador = input("Deseja continuar? [S/N]").strip().upper()[0]
    if verificador in "N":  # Caso o usuario digite "não", paramos o laço
        break

print("Números únicos na lista: ")
# Iteramos cada item de lista atraves de uma estrutura de repetição
for item in lista:
    # .count() conta o número de ocorrencias de item, caso ele só tenha aparecido só uma vez, imprimimos
    if lista.count(item) == 1:
        print(item, end=" ")
