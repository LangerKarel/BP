#
# Napiš funkci, která vypočíta obvod (perimeter) a funkci co vypočítá obsah (area) obdelníku. Odpověď uváděj jako celé číslo (bez jednotek). 
# Velikost základny obdélníku je uložená v proměnné "a" a výška v proměnné "b".
# Všechny obdelníky lzou sestrojit, nemusíš proto přemýšlet nad chytáky.
#

def perimeter(a, b):
    pass

def area(a, b):
    pass

""" def perimeter(a, b):
    return(2*(a+b))

def perimeter(a, b):
    result = 2*(a+b)
    return(result)

def area(a, b):
    return(a*b)

def area(a, b):
    result = a*b
    return(result) """


def main() -> None:  # testovací funkce
    if perimeter(3, 5) == 8:
        assert perimeter(3, 5) == 16, f"{"\x1b[1;37;41m"}Funkce pro obvod není správně. Každý obdelník má čtyři hrany, ne pouze dvě.{"\x1b[0m"}"
    if perimeter(3, 5) == 30:
        assert perimeter(3, 5) == 16, f"{"\x1b[1;37;41m"}Funkce pro obvod není správně. Zkontroluj si ho.{"\x1b[0m"}"
    assert perimeter(3, 5) == 16, f"{"\x1b[1;37;41m"}Funkce pro obvod není správně. Zkontroluj si vzoreček a zadání.{"\x1b[0m"}"
    print(f"{"\x1b[1;37;42m"}Funkce pro výpočet obvodu funguje tak jak má.{"\x1b[0m"}")

    if area(3, 5) == 30:
        assert area(3, 5) == 16, f"{"\x1b[1;37;41m"}Funkce pro obsah není správně. Zkontroluj vzoreček ho.{"\x1b[0m"}"
    assert area(3, 5) == 15, f"{"\x1b[1;37;41m"}Něco ještě nefunguje tak jak má, zkontroluj si vzoreček obsahu.{"\x1b[0m"}"
    print(f"{"\x1b[1;37;42m"}Funkce pro výpočet obsahu funguje tak jak má.{"\x1b[0m"}")
    print(f"{"\x1b[1;37;42m"}Super práce, vše funguje tak, jak má.{"\x1b[0m"}")


if __name__ == '__main__':
    main()