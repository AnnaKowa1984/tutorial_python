# klasa- to pewnego rodzaju foremka, przepis, który umożliwia nam stworzenie konkretnego przedstawiciela danej klasy, czyli obiektu
# obiekt jest konkretnym przedstawicielem danej klasy

# definiujemy naszą pierwszą klasę, korzystam ze słowa kluczowego class
# następnie podajemy nazwę naszej klasy - w tym przypadku jest to pies, dwukropek
# nasz klasa może zawierac pola, czyli jakies informacje o konkretnej klasie, informacje charakterystyczne dla wszystkich obiektów w tej klasie, informacje wspólną
# pole tworzymy poprzez zdefoniowanie zmiennej o konkretnej nazwie - u nas będzie to gatunek i możemy przypisac do tej zmiennej konkretna wartość
# klasa poza polami może równiez zawierać metody charakterystyczne dla konkretnej klasy oraz metody specjalne,
# np metoda __init__, która jestwywoływania podczas tworzenia nowego obiektu z klasy
# metoda __init__ przyjmuje specjalny parametr self, który odnosi się do nowotworzonego obiektu z danej klasy
# (czyli odwołując się do self, odwołujemy się do nowostworzonego obiektu i korzystając z self możemy zadeklarować jakies pola w naszym obiekcie
# -> pola charakterystyczne juz dla konkretnego przedstawiciela naszej klasynczyli dla obiektu)

# w naszym obiekcie zdefiniujemy nowe pola - pole rasa (od razu przypiszemy sobie wartość do tego pola)
# do naszej metody init dodamy 3 dodatkowe parametry: rasa, imie, wiek - te parametry bedziemy przekazywali podczas tworzenia naszego obiektu


class Pies:

    gatunek = "pies domowy"

    def __init__(self, rasa, imie, wiek):
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

#  teraz stworzymy nas pierwszy obiekt - jak to zrobic?
# aby stworzyć taki obiekt będziemy musieli odwołac się do naszej klasy i podac odpwiednie parametry, które zdeklarowaliśmy w metodzie __init_

# najpierw podajemy nazwę naszego obiektu - reksio
# i następnie tworzymy pierwszy obiekt, odwołujemy się do nazwy klasy i podajemy 3 argumanty zadeklarowane w metodzie __init__
# nie musimy tutaj podawć self, ponieważ odnosi sie ono do tworzonego pbiektu, w tym momencie tworzymy nowy obiekt, czyli self bedzie sie w naszym przypadku odnosiło do reksia

reksio = Pies("kundelek", "Reksio", 2)

#  teraz będziemy mogli wypisac sobie wartości dla naszego obiektu, czyli dla Reksia

print(reksio.wiek)
print(reksio.imie)
print(reksio.rasa)

#  możemy też wypisać gatunek, czyli pole, które jest charakterystyczne dla całej klasy
# korzystamy ponownie z metody print i możemy do tego pola odwołac sie z poziomu obiektu, czyli z poziomu reksia, ale
# równie dobrze możemy się do tego pola odwołać, kozystając z nazwy klasy, czyli Pies.gatunek, poniewaz jest to pole charakterystyczne dla całej klasy a nie dla konkretnych obiektów

print(reksio.gatunek)
print(Pies.gatunek)

#  teraz jeszcze spróbujemy odwołać sie do pola , które jest charakterystyczne dla obiektu z poziomu klasy

# print(Pies.wiek)
# wyskoczuył błąd: AttributeError: type object 'Pies' has no attribute 'wiek'

# nasza klasa Pies nie ma takiego pola jak wiek
# pole wiek jest charakterystyczne dla obiektu a nie dla klasy
# polem charakterystycznym dla klasy jest pole : gatunek
# i każdy obiekt który zostanie stworzony z tej klasy, bedzie miał dostep do pola gatunek, ponieważ jest to wartość, która będzie współdzielona między wszystkimi obiektami
# i każdy obiekt będzie róniez zawierał to pole
