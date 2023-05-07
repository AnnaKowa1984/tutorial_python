# słowo kluczowe return, które umożliwi zwrócenie wrośći z naszej metody

# tworzymy metodę dodawanie, która jako parametry będzie miała 2 liczby:
# wewnatrz ciala metody definiujemy return, który wypisze nam sumę tych 2 liczb
# pod deklaracją tej metody stworzymy zmienną 'suma' i następnie przypiszemy do niej wartość, która zostania zwrócona z funkcji dodawanie

# def dodawanie(pierwsza, druga):
#     print(pierwsza + druga)

# suma = dodawanie(2,2)
# print(suma)


# suma =  None
# mamy informację, że funkcja dodawanie nie zwraca żadnej wartości,
# ponieważ wewnatrz naszej metody dodawanie wypisujemt tylko wartość sumy na ekranie, ale nie zwracamy żadnej wartości
# żeby zwrócić wartośc musimy zamiast print w ciele funkcji wypisać return
# słowo kluczowe return zwróci nam coś z metody

def dodawanie(pierwsza, druga):
    return pierwsza + druga

pierwsza_suma = dodawanie(2, 2)
druga_suma = dodawanie(1, 1)

print(pierwsza_suma + druga_suma)
print(dodawanie(2, 2) + dodawanie(1, 1))