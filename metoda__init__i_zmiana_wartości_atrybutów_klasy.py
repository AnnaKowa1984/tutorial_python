# w tym cwiczeniu udowodnimy, że metoda init jest wykonywana podczas tworzenia nowego obiektu
# oraz spróbujemy, czy uda nam się nadpisac wartości konktretnych pól
# dla utworzonego wcześniej obiektu, dla obiektu Reksio

#  na poczatku dodajemy printa wewnatrz naszej metody init, aby sprawdzić czy ta metoda rzeczywoście jest wywoływana podczas twozrenia obiektu - wyprintowało się

# teraz sprawdzimy, jak sie ma sprawa z nadpisywaniem wartości konkretnych pół
# mamy obiekt typu pies, klasy pies, konkretnyobiekt reksio
# zdefiniowaliśmy konkretne wartości pól, mamy wiek 2 , spróbujemy teraz odwołać się do pola wiek i przypisac do niego wartość 3

class Pies:

    gatunek = "pies domowy"

    def __init__(self, rasa, imie, wiek):
        print("Wewnatrz metody init")
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek


reksio = Pies("kundelek", "Reksio", 2)

print(reksio.wiek)
reksio.wiek = 3
print(reksio.wiek)

#  wartość została nadpisana

#  sprawdzimy jeszcze jak sprawa się ma z polami, które są charakterystyczne dla klasy a nie dla konkretnego obiektu
#  mowa jest o gatunku
#  wypisujemy sobie reksio.gatunek  a następnie zmieniamy gatunke na "Ptak" z "Psa domowego", możemy sie odwoływać do konkretnego obiektu
#  i wypisujemy na ekraniewartość tego pola ponownie - wartość pola gatunek została nadpisana i teraz wynosi: ptak

print(reksio.gatunek)
reksio.gatunek = "ptak"
print(reksio.gatunek)

# jak widac, udalo sie udowodnic, że metoda init jest wykonywana podczas tworzenia nowego obiektu oraz, że nie ma problemu, aby napdpisać wartości pół stworzonego wcześniej obiektu,
# czyli wartości pól, które są tworzene wewnątrz metody init można bez problemu nadpisac w późniejszym toku naszego programu,
# oraz nie ma równiez problemu aby nadpisć wartośc pól charakterystycznych dla klasy