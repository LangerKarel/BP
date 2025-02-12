#
# Napiš funkci, která vrátí hodnotu True, pokud je obchod otevřený a False, pokud je obchod zavřený.
# Obchod otvírá v 8 hodin a zavírá ve 20 hodin. Aktuální čas bude vždy udán celým číslem a uložen v proměnné "current_hour".
# Pro psaní funkce smažte slovo "pass" a editujte svojí funkci.
#

def opening_hours(current_hour):
    pass

""" def opening_hours(current_hour):
    return(8<=current_hour<=20) """

""" def opening_hours(current_hour):
    return(8<=current_hour and current_hour<=20) """

""" def opening_hours(current_hour):
    if 8<=current_hour and current_hour<=20:
        return True
    else:
        return False """


def main() -> None:  # testovací funkce
    assert opening_hours(12) == True, f"{"\x1b[1;37;41m"}Něco se asi nepovedlo, zkontroluj si funkci ještě jednou.{"\x1b[0m"}"
    assert opening_hours(7) == False, f"{"\x1b[1;37;41m"}Zdá se, že tvůj obchod otvírá moc brzo.{"\x1b[0m"}"
    assert opening_hours(21) == False, f"{"\x1b[1;37;41m"}Zdá se, že tvůj obchod je otevřený i po zavírací době.{"\x1b[0m"}"
    assert opening_hours(8) == True, f"{"\x1b[1;37;41m"}Ujisti se, jestli obchod otvírá hned první hodinu.{"\x1b[0m"}"
    assert opening_hours(20) == True, f"{"\x1b[1;37;41m"}Ujisti se, jestli má obchod otevřeno i poslední hodinu.{"\x1b[0m"}"
    print(f"{"\x1b[1;37;42m"}Super práce, vše funguje tak, jak má.{"\x1b[0m"}")


if __name__ == '__main__':
    main()