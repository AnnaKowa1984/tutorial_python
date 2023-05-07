imiona = ["Ania", "Tomek", "Andrzej", 1, 2, 3, 4, 5]   # listy w Pythonie nie muszą zawierać jednego typu danych

print(imiona[0])    # odwołujemy sie w nawiasie kwadratowym do konkretnego indeksu
print(imiona[6])
print(imiona[-1])   # odwołanie sie do ujemnegoo indeksu - wyświetla sie pierwszy od końca
print(imiona[0:4])

print(imiona.index("Andrzej"))

imiona.append("Wojtek")     # dodaje element do listy na końcu
imiona.insert(0, "Grzegorz")    # jezeli chcemy dodać element w konkretnym miejscu (index, parametr)
                                # za pomocą metody insert mamy możliwość okrreślenia, gdzie konkretnie element ma byc dodany

print(imiona)

print(len(imiona))          # sprawdzenie długości listy - korzystamy z metody len
imiona.remove("Ania")       # usunięcie elementu z listy
print(imiona)

del imiona[0]               # słowo kluczowe del i nazwa listy z indexem - tez usuwa elementy listy
print(imiona)


# operacje na listach

pierwsza_lista = ["lampa", "koc", "krzesło"]
druga_lista = ["auto", "młotek", 1, 2, 3, 4]


print(pierwsza_lista * 3)   # mnożymy liste * 3
print(pierwsza_lista + druga_lista)     # dodajemy listy do siebie

