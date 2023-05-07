jezyki_programowania = ("js", "php", "java")

print(jezyki_programowania[0])
print(jezyki_programowania[-1])
print(jezyki_programowania[0:1])

# jezyki_programowania[0]="C#"

print(type(jezyki_programowania))


jezyki_programowania = "js", "php", "java"
print(type(jezyki_programowania))

jezyki_programowania = "js",        # string z przecinkiem, to krotka, która jest nieedytowalna, niemutowalna
print(type(jezyki_programowania))

jezyki_programowania = "js"         # string bez przecinka to string
print(type(jezyki_programowania))

jezyki_programowania = "js", 1, 2, 3, 4         # krotka może zawierać różne typy danych
print(type(jezyki_programowania))