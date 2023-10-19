i = 1
lista = []

while True:
    num = int(input(f"Digite o {i}º valor da lista: "))
    lista.append(num)
    i += 1
    verificador = input("Deseja continuar? [S/N]").strip().upper()[0]
    if verificador in "N":
        break

print("Números únicos na lista: ")
for item in lista:
    if lista.count(item) == 1:
        print(item, end=" ")
