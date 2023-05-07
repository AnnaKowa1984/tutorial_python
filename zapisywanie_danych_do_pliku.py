# jako parametr przy 'open' podamy nazwę pliku, który jeszcze nie istnieje
# jako drugi parametr podamy tryb, w jakim ten plik otwieramy -> 'w' od write
# następnie na zmiennej file wykonujemy metodę .write(), i jako parametr tej metody podaajemy tekst jaki chcemy wprowqadzić do pliku
# na końcu zamykamy plik korzystając z metody .close()

# tekst pierwotny : to jest jakis tekst
# zamienim ten tekst na : całkiem nowy tekst; żeby sprawdzić czy doda się nowa linia, czy tez pierwotny tekst zostanie nadpisany
            # pierwotny tekst został nadpisany

file = open("nowy.txt", "a")
file.write("całkiem nowy tekst. ")
file.close()

# aby dodać nowy tekst jako nową linie a nie nadpisywac wcześniejszego tekstu należy zmienic tryb na 'a' - append - dodaj
