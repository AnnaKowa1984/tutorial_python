imie = 'Ania'
nazwisko = "Kowalska 'Nowak' "
adres = '''Kwiatowa 12c/2
           Warszawa 02-213'''

print(nazwisko)

print('Czytam ksiazke "Wladce pierscieni" ')
print('Czytam ksiazke \n \"Wladce pierscieni\" ')       # backslash mówi o tym, ze wprowadzamy znak specjalny
                                                        # \n znak nowej linii
print('Czytam \t ksiazke \n \"Wladce pierscieni\" ')    # \t -> Tab
print(r'Czytam \t ksiazke \n \"Wladce pierscieni\" ')    # jeżeli dodamy r na początku, to te znaki specjalne nie są interpretowane

# żeby wypisać slash to musimy dać informację że wprowadzamy znak specjalny (\) i dopiero slash'a
print("\\")

print("małe litery".upper())    # zamienia wszystkie litery na DUZE
print("DUZE LITERY".lower())    # zamienia wszystkie litery na MASŁE

imie.islower()                  # sprawdza czy litery w stringu sa male
nazwisko.isupper()              # sprawdza czy litery w stringu sa duze

print(imie.islower())
print(nazwisko.isupper())

# teraz przeliterujemy po wszystkich literach w słowie

for char in "Ania":
    print(char)

print(imie[0])
print(imie[0:2])
print(imie.index("a"))
print("Ala" in "Ala ma kota")
print("Kasia" in "Ala ma kota")
print("Kasia" not in "Ala ma kota")

print(" ".join(["Ala", "ma", "kota"]))      # metoda .join() łaczy wyrazy jakie podamy w liście za pomocą tego, co jest w ""
print(" OK ".join(["Ala", "ma", "kota"]))

print(("Ala, ma, kota, i, psa").split(","))     # metoda .split() jest to kolejna metoda, którą możemy wywołać na stringach,
                                                # z wyrazów w stringu rozdzielonych separatorem zostanie zwrócona lista pojedynczych wyrazów

# metoda sprawdzająca czy string zaczyna się od odpowiednich liter
print(imie.startswith("An"))

# metoda sprawdzająca czy string kończy się odpowiednimi literami
print(imie.endswith("ia"))