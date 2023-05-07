class Sztucce:

    rodzaj = "zastawa stołowa"

    def __init__(self, firma, material, ilosc, cena):
        self.firma = firma
        self.material = material
        self.ilosc = ilosc
        self.cena = cena


zestaw1 = Sztucce("Swarowski", "srebro", 24, 460)
zestaw2 = Sztucce("Fork", "zloto", 36, 740)

print(zestaw1.firma)
print(zestaw1.material)
print(zestaw1.ilosc)
print(zestaw1.cena)
print(Sztucce.rodzaj)

print()

print(zestaw2.firma)
print(zestaw2.material)
print(zestaw2.ilosc)
print(zestaw2.cena)
print(zestaw2.rodzaj)
