def sortowanie_przez_wstawianie(lista, n):
    for i in range(1, n):
        pom = lista[i]          # element do wstawienia
        j = i - 1

        # przesuwanie elementów większych od pom
        while j >= 0 and lista[j] > pom:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = pom      # wstawienie w odpowiednie miejsce


# Główna część programu
n = int(input("Podaj wielość zbioru: "))
lista = []

for i in range(n):
    lista.append(int(input()))

sortowanie_przez_wstawianie(lista, n)

# Wyświetlenie posortowanej listy
print(*lista)