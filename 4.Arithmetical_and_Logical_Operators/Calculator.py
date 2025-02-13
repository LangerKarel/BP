#
# Napiš čtyři funkce základních matematických operací - sčítání (addition), odčítání (subtraction), násobení (multiplication) a dělení (division).
# Každá funkce dostane na vstup dvě celá čísla uložená v proměnných "x" a "y". Může však vrátit i číslo s desetinou čárkou.
# Při řešení funkcí operací u kterých záleží na pořádí použij "x" jako první (menšenec a dělenec).
# Pokud příklad nelze vypočítat, vrať hodnotu "False".
#

def addition(x, y):
    pass

def subtraction(x, y):
    pass

def multiplication(x, y):
    pass

def division(x, y):
    pass

""" def addition(x, y):
    return(x + y)

def addition(x, y):
    result = x + y
    return(result)

def subtraction(x, y):
    return(x - y)

def subtraction(x, y):
    result = x - y
    return(result)

def multiplication(x, y):
    return(x * y)

def multiplication(x, y):
    result = x * y
    return(result)

def multiplication(x, y):
    result = 0
    for i in range(y):
        result += x
    return(result) 

def division(x, y):
    return(y and x / y or False)

def division(x, y):
    if y == 0:
        return(False)
    return(x / y)

def division(x, y):
    if y == 0:
        return(False)
    else:
        result = x / y
    return(result) """


def main() -> None:  # testovací funkce
    assert addition(12, 5) == 17, f"{"\x1b[1;37;41m"}Funkce sčítání nefunguje správně.{"\x1b[0m"}"
    print(f"{"\x1b[1;37;42m"}Funkce sčítání funguje správně.{"\x1b[0m"}")

    if subtraction(12, 5) == -7:
        assert subtraction(12, 5) == 7, f"{"\x1b[1;37;41m"}Zkontroluj správné pořádí číslic podle zadání.{"\x1b[0m"}"
    assert subtraction(12, 5) == 7, f"{"\x1b[1;37;41m"}Funkce odčítání nefunguje správně.{"\x1b[0m"}"
    print(f"{"\x1b[1;37;42m"}Funkce odčítání funguje správně.{"\x1b[0m"}")

    assert multiplication(5, 3) == 15, f"{"\x1b[1;37;41m"}Funkce násobení nefunguje správně.{"\x1b[0m"}"
    print(f"{"\x1b[1;37;42m"}Funkce násobení funguje správně.{"\x1b[0m"}")

    if subtraction(3, 15) == 5:
        assert subtraction(15, 3) == 5, f"{"\x1b[1;37;41m"}Zkontroluj správné pořádí číslic podle zadání.{"\x1b[0m"}"
    assert division(15, 3) == 5, f"{"\x1b[1;37;41m"}Funkce dělení nefunguje správně.{"\x1b[0m"}"
    assert division(15, 0) == False, f"{"\x1b[1;37;41m"}Funkce dělení nefunguje správně.{"\x1b[0m"}"
    print(f"{"\x1b[1;37;42m"}Funkce dělení funguje správně.{"\x1b[0m"}")

    print(f"{"\x1b[1;37;42m"}Super práce, vše funguje tak, jak má.{"\x1b[0m"}")


if __name__ == '__main__':
    main()