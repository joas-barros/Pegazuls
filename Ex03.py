i = 1
lista = []

while True:
    num = int(input(f"Digite o {i}º valor da lista: "))
    lista.append(num)
    i += 1
    verificador = input("Deseja continuar? [S/N]").strip().upper()[0]
    if verificador in "N":
        break

lista = sorted(lista)
lista_unica = list()
lista_unica.append(lista[0])
for i in range(1, len(lista) - 1):
    if lista[i] != lista[i - 1]:
        lista_unica.append(lista[i])

print(lista_unica)
