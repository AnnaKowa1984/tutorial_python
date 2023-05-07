pierwszy_zbior = {"Warszawa", "Kraków", "Katowice", "Lodz"}
drugi_zbior = {"Warszawa"}

pierwszy_zbior.add("Kielce")    # dodajemy nowy, unikalny element
print(pierwszy_zbior)

pierwszy_zbior.add("Lodz")      # zbiór przechowuje elementy tylko unikalne, drugi raz dodana Lodz nie wyświetli się powtórnie
print(pierwszy_zbior)

# teraz odwołamy się z elementu zbioru korzystając z indeksu
# print(pierwszy_zbior[0])    # wyskakuje błąd zbiór nie wspiera indeksowania, czyli elementy w zbiorze nie mają porządku


# operacje na zbiorach

print(pierwszy_zbior - drugi_zbior)     # odejmowanie zbiorów
print(pierwszy_zbior | drugi_zbior)     # suma zbiorów   (shift + \)
print(pierwszy_zbior & drugi_zbior)     # część wspólna dwóch zbiorów
print(pierwszy_zbior ^ drugi_zbior)     # różnica symetryczna  - dwóch zbiorów to taka, gdzie dany element występuje w jednym lub w drugim zbierze, ale nie w obu na raz
