# słowniki, które zawieraja pary klucz:wartość
# klucze muszą mieć wartości unikalne

dziennik = {1:"Kowalski", 2:"Nowak", 3:"Lewandowski"}

# aby sie odwołać do konkretnej wartości, korzystamy z metody get i podajemy klucz
print(dziennik.get(1))
print(dziennik[1])

dziennik[4] = "Mucha"       # aby zdefiniować nowy element, odwołujemy się do zmiennej dziennik a następnie tworzymy nowy klucz i przypisujemy do niego wartość
print(dziennik[4])

# przeiterujemy teraz (przechodzimy) po wszystkich kluczach
# dziennik ma metodę .keys() - klucze
for key in dziennik.keys():
    print(key)

# możemy również przeiterować po wartościach
for value in dziennik.values():
    print(value)

del dziennik[1]     # usuwanie elementu ze słownika - używamy słowa kluczowego del i następnie wskazujemy ten element przy użyciu [] i odpowiedniego klucza
for value in dziennik.values():
    print(value)

dziennik[2] = "Nowy uczeń" # dla elementu dziennika z kluczem 2 aktualizujemy wartość elementu na Nowy uczeń
print("Nowy uczeń to " + dziennik[2])