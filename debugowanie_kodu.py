# debugowanie kodu - możliwość zatrzymania wykonywania programu w dowolnym miejscu, określonym przez nas,
# żeby sprawdzić czy np. zmienne, które zdefinopwaliśmy, zostały odpwiednio zainicjaliowane i mają odpowiednią wartość

# wykonując takie debugowanie w teście Selenium, można śledzić aplikacje webową, to co dzieje się w przeglądarce

#  żeby rozpocząć debugowanie najpierw trzeba zaznaczyć punkt, w którym trzeba się zatrzymać, tzw. break piont, klikając myszką po lewej stronie - pojawiają się czerwone kropki

while True:
    try:
        print("Podaj pierwsza liczbe: ")
        pierwsza_liczba = int(input())

        print("Podaj druga liczbe: ")
        druga_liczba = int(input())

        print(pierwsza_liczba + druga_liczba)
        break   # przerwie nasz program, gdy wartość nadawania zostanie zwrócona

    except ValueError:
        print("Podałeś błędną wartość. ")
        print("Spróbuj jeszcze raz.")
        continue

# Przy naciśnięciu na przycisk Play, nic sie nie stanie, kod się wykona.
# Aby zatrzymac kod w odpowiednim miejscu, musimy wybrac znak "robaczka" - debug

# program napotyka na break point, odpowiednią linijkę mamy zakreśloną, i zatrzymuje się
# na dole widzimy informację o naszych liczbach : Special Variables charakterystyczne dla Pythona i pierwsza_liczba z przypisana do niej wartością
# aby przejść do kolejnego break pointu możemy wybrać F9 na klawiaturze lub kliknąć zielony przycisk |> po lewej stronie /nie działa ;( /