from Wychowawca import Wychowawca
from Nauczyciel import Nauczyciel
from Uczen import Uczen

uczniowie = []
nauczyciele = []
wychowawcy = []


def utworz_ucznia():
    imie = input("Podaj imię ucznia: ")
    nazwisko = input("Podaj nazwisko ucznia: ")
    klasa = input("Podaj klasę ucznia (np. 3C): ")
    uczniowie.append(Uczen(imie, nazwisko, klasa))


def utworz_nauczyciela():
    imie = input("Podaj imię nauczyciela: ")
    nazwisko = input("Podaj nazwisko nauczyciela: ")
    przedmiot = input("Podaj nazwę przedmiotu prowadzonego przez nauczyciela: ")
    klasy = input("Podaj nazwy klas, które prowadzi nauczyciel (oddzielone przecinkiem): ").split(',')
    nauczyciele.append(Nauczyciel(imie, nazwisko, przedmiot, klasy))


def utworz_wychowawce():
    imie = input("Podaj imię wychowawcy: ")
    nazwisko = input("Podaj nazwisko wychowawcy: ")
    klasa = input("Podaj nazwę klasy, której jest wychowawcą: ")
    wychowawcy.append(Wychowawca(imie, nazwisko, klasa))


def zarzadzaj_klasa():
    klasa = input("Podaj nazwę klasy: ")
    print(f"\nUczniowie w klasie {klasa}:")
    for uczen in uczniowie:
        if uczen.klasa == klasa:
            print(f"{uczen.imie} {uczen.nazwisko}")
    print("\nWychowawca klasy:")
    for wychowawca in wychowawcy:
        if wychowawca.klasa == klasa:
            print(f"{wychowawca.imie} {wychowawca.nazwisko}")


def zarzadzaj_uczniem():
    imie = input("Podaj imię ucznia: ")
    nazwisko = input("Podaj nazwisko ucznia: ")
    for uczen in uczniowie:
        if uczen.imie == imie and uczen.nazwisko == nazwisko:
            print(f"Lekcje ucznia {imie} {nazwisko} w klasie {uczen.klasa}:")
            for nauczyciel in nauczyciele:
                if uczen.klasa in nauczyciel.klasy:
                    print(f"- Lekcja: {nauczyciel.przedmiot}, Nauczyciel: {nauczyciel.imie} {nauczyciel.nazwisko}")


def zarzadzaj_nauczycielem():
    imie = input("Podaj imię nauczyciela: ")
    nazwisko = input("Podaj nazwisko nauczyciela: ")
    for nauczyciel in nauczyciele:
        if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko:
            print(
                f"Nauczyciel {imie} {nazwisko}, przedmiot: {nauczyciel.przedmiot}, klasy: {', '.join(nauczyciel.klasy)}")


def zarzadzaj_wychowawca():
    imie = input("Podaj imię wychowawcy: ")
    nazwisko = input("Podaj nazwisko wychowawcy: ")
    for wychowawca in wychowawcy:
        if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko:
            klasa = wychowawca.klasa
            print(f"Uczniowie prowadzeni przez wychowawcę {imie} {nazwisko} w klasie {klasa}:")
            for uczen in uczniowie:
                if uczen.klasa == klasa:
                    print(f"{uczen.imie} {uczen.nazwisko}")


while True:
    print("\nMenu główne:")
    print("1. Utwórz")
    print("2. Zarządzaj")
    print("3. Koniec")
    wybor = input("Wybierz opcję (1-3): ")

    if wybor == "1":
        print("\nProces tworzenia użytkowników:")
        print("1. Uczeń")
        print("2. Nauczyciel")
        print("3. Wychowawca")
        print("4. Koniec")
        opcja = input("Wybierz opcję (1-4): ")

        if opcja == "1":
            utworz_ucznia()
        elif opcja == "2":
            utworz_nauczyciela()
        elif opcja == "3":
            utworz_wychowawce()
        elif opcja == "4":
            continue
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")

    elif wybor == "2":
        print("\nProces zarządzania użytkownikami:")
        print("1. Zarządzaj klasą")
        print("2. Zarządzaj uczniem")
        print("3. Zarządzaj nauczycielem")
        print("4. Zarządzaj wychowawcą")
        print("5. Koniec")
        opcja = input("Wybierz opcję (1-5): ")

        if opcja == "1":
            zarzadzaj_klasa()
        elif opcja == "2":
            zarzadzaj_uczniem()
        elif opcja == "3":
            zarzadzaj_nauczycielem()
        elif opcja == "4":
            zarzadzaj_wychowawca()
        elif opcja == "5":
            continue
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")

    elif wybor == "3":
        print("Koniec programu.")
        break

    else:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")
