 # ten temat pokaże, jak zaimportowac moduł Pythona do pliku, aby móc korzystać z metod, które są dostępne w konkretnym module
 # stworzymy generator liczb losowych
 # skorzystamy z modułu random, który umożliwi nam wygenerowanie liczby losowej

 # aby móc korzystać z kodu zawartego w module random, musimy ten moduł zaimportować
 # korzystamy ze słowa kluczowego import, następnie podajemy nazwę modułu, który chcemy zaimportować


 # teraz zdefiniujemy metodę: generuj liczbę
 # jako paramter podajemy max wartość takiej liczby
 # nasza metoda będzie zwracała wygenrowana liczbe losową
 # skorzytsamy tu z metody randint, która przyjmuje 2 argumenty min i max
 # min to wartość minimalna, max to wartość maxymalna
 #  przekazujemy min i max do wywołania naszej metody randint
 #  i w taki oto sposób mamy metodę, która wygeneruje nam liczbe losową


import random

def generuj_liczbe(min, max):
    return random.randint(min, max)

 # teraz wypiszemy na ekranie wygenerowaną liczbę, zakres od 0 do 100

print(generuj_liczbe(0,100))


 # możemy też to zrobić w pętli i wygenerować 20 takich liczb losowych (zakresu 0-20) o wartościach 0-100


for i in range(0,20):
    print(generuj_liczbe(0,100))