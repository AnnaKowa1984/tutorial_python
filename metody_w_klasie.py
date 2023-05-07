# W tym odcinku dodamy 2 nowe metody do klasy: pies
# metodę : szczekaj
# oraz metodę: zaprezentuj psa.

# W poprzedniej lekcji stworzyliśmy metodę init, które była odpalana przy tworzeniu nowego obiektu danej klasy



class Pies:

    gatunek = "pies domowy"

    def __init__(self, rasa, imie, wiek):
        print("Wewnatrz metody init")
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

# Teraz definiujemy metodę: szczekaj,  def szczekaj
# jako parametr ta metoda przyjmuje self, który umożliwia nam odwołanie sie do konkretnych pól danego obiektu
# i wewnatrz tej metody wypisujemmy na ekranie: hau, hau
# korzystamy z metody print i wypisujemy hau, hau


    def szczekaj (self):
        print("Hau! Hau!")   # pojawi sie wartość none, ponieważ nic nie zwracamy, tylko wyprintowujemy
        return("Hau! Hau!")

# Druga metoda : zaprezentuj psa
# tutaj równiez jako parametr przekazujemy self
# i w tym przypadku skorzystamy z wczesneij zdefiniowanych pól: rasa , imie, wiek
# w przypadku wieku musimy pamiętac o zrzutowaniu intigera na stringa

    def zaprezentuj_psa(self):
        print("Rasa to " + self.rasa)
        print("Imie to " + self.imie)
        print("Wiek psa to " + str(self.wiek))


reksio = Pies("kundelek", "Reksio", 2)

# print(reksio.wiek)
# reksio.wiek = 3
# print(reksio.wiek)
#
# print(reksio.gatunek)
# reksio.gatunek = "ptak"
# print(reksio.gatunek)

print(reksio.szczekaj())
print(reksio.zaprezentuj_psa())
