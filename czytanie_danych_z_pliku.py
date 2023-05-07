# wewnątrz pliku tworzymy zmienna file i korzystamy z metody 'open'
# jako parametr podajemy nazwę naszego  pliku - tak naprawdę ścieżkę do pliku, ale jesteśmy w tym wypadku na tej samej ścieżce
# tworzymy zmienna zawartość i wywołujemy na niej metodę .read()
# wypisujemy zmienną zawartość na ekranie
# i nastepnie zamykamy plik korzystając z metody .clese()

file = open("wiadomosc.txt")
zawartosc = file.read()
print(zawartosc)
file.close()
print()
# inne metody za pomocą których można czytac pliki w Pythonie
 
file = open("wiadomosc.txt")
zawartosc = file.readlines()    # metoda .readlines(), którą wywołujemy na pliku - zwraca listę z kolejnymi liniami pliku
print(zawartosc)
file.close()
print()

file = open("wiadomosc.txt")
zawartosc = file.readline()    # metoda .readline(), czyta pierwsza linię pliku
print(zawartosc)
file.close()
print()

# możemy skorzytać tez z innego zapisu - skorzystamy z pętli for

file = open("wiadomosc.txt")

for line in file:    #wypisujemy linie, które znajdują się w pliku
    print(line)

