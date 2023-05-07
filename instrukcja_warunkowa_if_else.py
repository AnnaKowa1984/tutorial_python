# blok else jest blokiem opcjonalnym
# jest wykonywany w przypadku, gdy warunek wykonywany w if ma wartość False
# jeśli if ma wartość True, to jest wykonywany if a blok else jest pomijany

print("Zmienna ma wartość False")
print()

glodny = False

if glodny:
    print("Jestem głodny czy już pora coś zjeść?")
    print("Otwieram lodówkę.")
else:
    print("Jestem najedzony.")
print()

print("Gdy zmienna ma wartość True")
print()

glodny = True

if glodny:
    print("Jestem głodny czy już pora coś zjeść?")
    print("Otwieram lodówkę.")
else:
    print("Jestem najedzony.")