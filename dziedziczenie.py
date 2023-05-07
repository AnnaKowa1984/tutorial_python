# dziedziczenie w Pythonie
#
# umożliwa zbudowanie pewnej hierarchii klas, w której będziemy mogli wyróżnić klasę nadrzędną (rodzica) i podrzędną (dziecko)
# klasa podrzędna będzie miała dostęp do pól i metod zdefiniowanych w klasie rodzica
#
# tworzymy klasę, która będzie klasą nadrzedną (Osoba)
# wewnatrz tej klasy definiujemy metodę init
# wewnątzr metody init stworzymy pola do których przypiszemy pewne wwrtości, podane jako parametry do metody init (imie i nazwisko)
# klasa osoba, obiekt tej klasy, będzie posiadał dwa pola - imię i nazwisko

class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


# jeszcze wewnątrz tej klasy zdefiniujemy metodę: przedstaw się
# metoda przedstaw się będzie zwracala informacje o danej osobie: Nazywam sie + odwołanie do imienia i nazwiska

    def przedstaw_sie(self):
        return "Nazywam sie " + self.imie + " " + self.nazwisko

# nastepnie tworzymy kolejna klasę, która będzie dzickiem osoby
# będzie dziedziczyła po tej klasie
# mamy klase student i aby okreslić, ze ta klasa jest klasą podrzedna i dziedziczy po klasie osoba, korzystamy z nawiasów okragłych i podajemy nazwę klasy po której dziedziczymy
# wewnatrz klasy student definiujemy również metodę init
# i przekażemy sobie do tej metody init kilka parametrów - imie, nazwisko i numer indeksu

# wewnatrz takiej metody init, wewnatrz klasy student, która dziedziczy po klasie osoba, będziemy mogli wywołać metody init z klasy osoba


class Student(Osoba):

    def __init__(self, imie, nazwisko, numer_indeksu):
        Osoba.__init__(self, imie, nazwisko)
        self.indeks = numer_indeksu

#  korzystamy z nazwy klasa - Osoba, następnie wywołujamy metodę init i przekazujemy odpowiednie parametry - self, imie i nazwisko
#  i nastepnie, wewnatrz jeszcze metody init, uwstawiamy pole indeks i przypisujemy do tego pola wartość - numer_indeksu


    def podaj_numer_indeksu(self):
        return self.indeks


#  definiujemy równiez w naszej klasie Student metodę: podaj numer indeksu
#  i zwracamy tutaj z naszej metody numer indeksu
#  tutaj jako parametr podajemy self i odwołujemy sie do pola indeks


#  teraz spróbujemy stworzyc obiekt klasy student i zobaczymy czy będziemy mieli odstęp do pól zdefiniowanych w klasie Osobaa oraz do metod zdefiniowanych w klasie Osoba

#  odwołujemy się do klasy, podajemy odpowiednie argumenty: imie, nazwisko i numer_indeksu

student = Student("Tomasz", "Kot", 123456)

# zobaczmy jeszcze czy uda nam sie wywołać metodę: przedstaw się, jest to metoda z klasy Osoba, którą dziedziczymy z tej klasy
# i oczywiście możemy tez odwołąc sie do metody, która jest zdefiniowana bezpośrodnio w klasie Student
# printem wypiszemy sobioe te informacje na ekranie

print(student.przedstaw_sie())
print(student.podaj_numer_indeksu())

#  w taki sposób zdefiniowaliśmy hierarchie w naszych klasach,
#  zdefiiowaliśmy sobie informacje o tym, że klasa Student dziedziczy po klasie Osoba i ma dostęp do metod oraz pól,
#  które zostały zdefiniowane w klasie Osoba, czyli w klasie nadrzędnej, w klasie rodzica