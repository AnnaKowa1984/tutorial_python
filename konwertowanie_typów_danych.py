# print("1" + 1)
# TypeError: can only concatenate str (not "int") to str

print("1" + str(1))

print(2 + int("2"))

print(2 + 2.4)

# print(2 + int("2.4"))
# ValueError: invalid literal for int() with base 10: '2.4'  -> stringa zmiennoprzecinkowego nie możemy przekonwertować do int'a'

print(2 + float("2.4"))

print("Mój tekst. " * 5)

# print("Mój tekst. " * "Ania")
# TypeError: can't multiply sequence by non-int of type 'str' -> nie można mnożyc stringa przez stringa