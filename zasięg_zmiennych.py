# scope of variables

imie = "Ania"       # zmienna globalna
nazwisko = "Nowak"  # zmienna globalna

def przedstaw_sie():        # zmienna lokalna wewnatrz metody
    nazwisko = "Kowalska"
    print(nazwisko)
    print(imie)

print(imie)         # Ania
print(nazwisko)     # Nowak

# zmienna nazwisko nie wyświetli się, ponieważ jest dostępna tylko lokalnie, tylko wewnątrz metody def
# dopiero po wywołaniu metody przedstaw_sie zostanie wyprintowane wszystko

przedstaw_sie()     # Kowalska, Ania
print(nazwisko)     # Nowak

# zmienna globalna nie została nadpisana przez zmienną lokalną