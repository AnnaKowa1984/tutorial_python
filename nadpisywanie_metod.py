#  w tym zagadnieniu omówione zostanie nadpisywanie metot
#  wewnatrz klay Student, czyli w klasie potomnej, zefiniujemy sobie metodę o takiej samej nazwie, jaka juz istnieje w klasie nadrzednej



class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "Nazywam sie " + self.imie + " " + self.nazwisko

class Student(Osoba):

    def __init__(self, imie, nazwisko, numer_indeksu):
        Osoba.__init__(self, imie, nazwisko)
        self.indeks = numer_indeksu

    def podaj_numer_indeksu(self):
        return self.indeks

#  mamy metodę przedstaw się, i taką samą metodę, o takiej samej nazwie zdefiniujemy w klasie Student i zobaczymy, która metoda zostanie wywołana w naszym skrypcie
# definiujemy metodę def przedstaw sie i wewnatrz tej metody zwrócimy inna wartość

    def przedstaw_sie(self):
        return "Jestem studentem i mam na imie " + self.imie

student = Student("Tomasz", "Kot", 123456)
print(student.przedstaw_sie())
print(student.podaj_numer_indeksu())

# na ekranie została wypisana nadpisana metoda, zostało wypisane na ekranie: Jestem studentem i mam na imie Tomasz
# czyli metoda zdefiniowana w klasie rodzica została przeslonięta przez metodę zdefiniowana w klasie Student



# Teraz zmienimy troszeczkę zachowanie i zamiast tworzyć obiekt typu Student, stworzymy obiekt typu: Osoba
# wykomentujemy kod z metodą charakterystyczna dla klasy student
# i teraz wywołamy metodę:przedstaw się

osoba = Osoba("Tomasz", "Kot")
print(osoba.przedstaw_sie())
# print(student.podaj_numer_indeksu())

#  i w takim przypadku, gdy tworzymy obiekt typu Osoba, to wywoływana jest metoda z klasy nadrzędnej
#  mamy wiec możliwość nadpisywania metod w klasach potomnych, nadpisywania zachowania metod definiując metody o takiej samej nazwie