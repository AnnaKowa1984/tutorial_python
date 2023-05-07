# defeiniujemy metodę rzeczy i jako parametr podajemy args (argument- konkretna wartość którą przekazujemy przy wywołaniu
# przy wywołaniu metody, konkretne wartosci, które podajemy , nazwane są argumentami , stad skrót args -argumenty
# agrs, jeżeli zdefiniujemy taki parametr to oznacze, ze możmy podać po przecinku kilka parametrów, jako listę, zbiór argumentów,
# i one po przeliterowaniu zostaną wszystkie wypisane na ekranie


def rzeczy(*args):
    for arg in args:
        print(arg)

rzeczy("lampa", "łóżko", "koc", "telefon")
print()



def rzeczy(pierwsza_rzecz, *args):
    print(pierwsza_rzecz)
    print(args[0])
    for arg in args:
        print(arg)

rzeczy("lampa", "łóżko", "koc", "telefon")