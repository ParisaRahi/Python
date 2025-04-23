a = input("Test inn et heltall! ")
b = int(a)
if b < 10:
    print(b + "Hei!")

# del 1 -> nei, koden stoppes i linje 4 siden int ikke kan konkateneres med string
# del 2 -> TypeError: unsupported operand type(s) for +: 'int' and 'str'