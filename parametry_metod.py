# parametry metod - możliwość przekazania jekiejs wartości do metody, która zostanie użyta w tej metodzie

def przedstaw_się(imie, wiek):
    print("Cześć mam na imię " + imie)
    print("Mam " + wiek)

przedstaw_się("Ania", "38 lat")
przedstaw_się("Tomek", "39 lat")






# przedstaw_się(1) - wyskoczy błąd, ponieważ 1 jest intem
# przedstaw_się(str(1))