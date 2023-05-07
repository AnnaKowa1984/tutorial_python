# wypisywanie na ekranie informacji z pliku pogodynka, który importujemy
# chcemy tylko importować Pogodynkę, nie chcemy wywoływać kodu, który się tam znajduje

# w PC, w pliku importowanym wpisujemy name, wybieramy enter, tworzy sie if i fdo tego if kopiujemy kod,
# który byl wczesniejwykonywany w pliku Pogodynka

# teraz możemy ponownie sprawdzic pogode i zobaczymy, czy tym razem kod zawarty w pliku pogodynka, zostanie wypisany
import selenium.
import pogodynka

def pogoda_krakow():
    return "Słonecznie"

def pogoda_szczecin():
    return "Pochmurno"

def pogoda_wroclaw():
    return "Upał"

# teraz wypiszmy na ekranie te wartości

# print(pogoda_krakow())
# print(pogoda_szczecin())
# print(pogoda_wroclaw())



if __name__ == '__main__':
    print("Witaj w prognozie pogody.")
    print("Pogoda w Krakowie: " + pogodynka.pogoda_krakow())
    print("Pogoda w Szczecinie: " + pogodynka.pogoda_szczecin())
    print("Pogoda we Wrocławiu: " + pogodynka.pogoda_wroclaw())
