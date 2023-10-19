i = 1
lista = []

while True:
    num = int(input(f"Digite o {i}º valor da lista: "))
    lista.append(num)
    i += 1

    # .strip() remove possiveis espaços que o usuario digitar
    # .upper() transforma tudo em maiuscula
    # [0] pois só queremos o primeiro caractere da string (S ou N)
    verificador = input("Deseja continuar? [S/N]").strip().upper()[0]
    if verificador in "N":
        break

print("Números únicos na lista: ")
for item in lista:
    if lista.count(item) == 1:
        print(item, end=" ")
