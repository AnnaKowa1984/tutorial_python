# parametry nazwane - **kwargs
# prametr kwargs umożliwia nam podawanie tzw. argumntów nazwanych, definiując nazwę argumentu i po znaku = przypisując do niego konkretną wartość

# kwargsy jako argumanety są argumentami nazwanymi i składaja się z par klucz-wartość (nazwa-wartość)
# te argumenty będą zapisane w specyficzny sposób, co umożliwi nam iterowanie po tych kluczach, czyli po nazwach tych parametrów

# metoda get -> umożliwia nam pobranie konkretnej wartości, korzystajać z odpowiedzniej nazwy parametru

def dziennik(klasa, **kwargs):
    print("Klasa " + klasa)
    for nazwisko in kwargs.keys():
        print(nazwisko)
    print(kwargs.get("Kowalski"))

dziennik("3c", Kowalski = 1 , Nowak = 2, Wiśniewski = 3)


