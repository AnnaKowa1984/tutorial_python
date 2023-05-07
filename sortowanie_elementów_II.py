# Sortowanie elementów - II

#Przedstawiona w poprzedniej lekcji metoda sort(), zmienia kolejność elementów w istniejącej liście.  Dla zapisu:

nazwiska = ["Kowalski", "Nowak", "Adamiak"]
nazwiska.sort()
print(nazwiska)

# na ekranie zostanie wypisana informacja:

    # ['Adamiak', 'Kowalski', 'Nowak']

# Jeżeli nie chcemy modyfikować kolejności elementów w istniejącej liście tylko stworzyć nową posortowaną listę to  korzystamy z metody sorted(lista).
# Ta metoda zwróci nam nową listę, która będzie posortowana. Początkowa lista pozostanie w niezmienionym stanie. Dla zapisu:

nazwiska = ["Kowalski", "Nowak", "Adamiak"]
posortowane = sorted(nazwiska)
print(nazwiska)
print(posortowane)

# na ekranie zostanie wypisana informacja:

    # ['Kowalski', 'Nowak', 'Adamiak']
    # ['Adamiak', 'Kowalski', 'Nowak']

# Widzimy tutaj, że pierwotna lista nie została posortowana.

# Metoda sorted(lista, reverse = True) umożliwia nam zmianę sposobu sortowania. Dla zapisu:

nazwiska = ["Kowalski", "Nowak", "Adamiak"]
posortowane = sorted(nazwiska, reverse=True)
print(nazwiska)
print(posortowane)

# na ekranie zostanie wypisana informacja:

    # ['Kowalski', 'Nowak', 'Adamiak']
    # ['Nowak', 'Kowalski', 'Adamiak']