while True:
    try:
        print("Podaj pierwszą liczbę: ")
        pierwsza_liczba = int(input())

        print("Podaj druga liczbę: ")
        druga_liczba = int(input())

        print(pierwsza_liczba + druga_liczba)
        break   # przerwie nasz program, gdy wartość nadawania zostanie zwrócona

    except ValueError:
        print("Podałeś błędną wartość, spróbuj jeszcze raz.")
        continue

# jako drugą liczbę wpisują stringa - wyskakuje błąd
# chcę, aby w takiej sytuacji użytkownik dostał informację, że podał błęde dane
# i umożliwiam mu podanie danych jeszcze raz
# stosuję try i except


# stworzymy pętlę while, która umożliwi nam wprowadzenie wartości od nowa