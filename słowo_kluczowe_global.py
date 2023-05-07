# słowo kluczowe global umożliwia nadpisanie wartości zmiennej globalnej wewnątrz metody przedstaw_się
# czyli nadpiszemy wartość zmiennej nazwisko zmieniajac tą wartość z Nowak na Kowalski


imie = "Ania"       # zmienna globalna
nazwisko = "Nowak"  # zmienna globalna

def przedstaw_sie():        # zmienna lokalna wewnatrz metody
    global nazwisko         # w taki sposób informujemy, że nazwisko odnosi się do zmiennej globalnej
                            # i gdy w tym momencie do zmiennej nazwisko przypiszemy nową wartość,
                            # to zostanie ta wartość globalna nadpisana
    nazwisko = "Kowalska"
    print(nazwisko)
    print(imie)

print(imie)         # Ania
print(nazwisko)     # Nowak

# zmienna nazwisko nie wyświetli się, ponieważ jest dostępna tylko lokalnie, tylko wewnątrz metody def
# dopiero po wywołaniu metody przedstaw_sie zostanie wyprintowane wszystko

przedstaw_sie()     # Kowalska, Ania
print(nazwisko)     # nadpisane nazwisko Kowalska