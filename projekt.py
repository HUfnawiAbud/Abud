from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.foglalt = False

    @abstractmethod
    def szoba_tipus(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 6000)

    def szoba_tipus(self):
        return "egyágyas"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)

    def szoba_tipus(self):
        return "kétágyas"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def szoba_foglalasa(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam and not szoba.foglalt and datum >= datetime.now():
                szoba.foglalt = True
                return szoba.ar
        return None

    def foglalas_lemondasa(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam and szoba.foglalt:
                szoba.foglalt = False
                return True
        return False

    def foglalasok_listazasa(self):
        foglalasok = []
        for szoba in self.szobak:
            if szoba.foglalt:
                foglalasok.append(szoba.szobaszam)
        return foglalasok

# Példa adatokkal feltöltött rendszer létrehozása
szalloda = Szalloda("Példa Szálloda")
szalloda.szoba_hozzaadasa(EgyagyasSzoba("101"))
szalloda.szoba_hozzaadasa(EgyagyasSzoba("102"))
szalloda.szoba_hozzaadasa(KetagyasSzoba("201"))
szalloda.szoba_hozzaadasa(KetagyasSzoba("202"))
szalloda.szoba_hozzaadasa(KetagyasSzoba("203"))

# Példa foglalások hozzáadása
szalloda.szoba_foglalasa("101", datetime.now() + timedelta(days=1))
szalloda.szoba_foglalasa("201", datetime.now() + timedelta(days=2))
szalloda.szoba_foglalasa("203", datetime.now() + timedelta(days=3))
szalloda.szoba_foglalasa("102", datetime.now() + timedelta(days=4))
szalloda.szoba_foglalasa("202", datetime.now() + timedelta(days=5))

# Felhasználói interfész
while True:
    print("\n1. Szoba foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Kilépés")
    valasztas = input("Válasszon műveletet: ")

    if valasztas == "1":
        szobaszam = input("Adja meg a szoba számát: ")
        datum_input = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        datum = datetime.strptime(datum_input, "%Y-%m-%d")
        ar = szalloda.szoba_foglalasa(szobaszam, datum)
        if ar:
            print(f"A foglalás sikeres. A szoba ára: {ar} Ft.")
        else:
            print("Nem sikerült foglalni a szobát.")
    elif valasztas == "2":
        szobaszam = input("Adja meg a lemondani kívánt foglalás szoba számát: ")
        if szalloda.foglalas_lemondasa(szobaszam):
            print("A foglalás sikeresen lemondva.")
        else:
            print("Nincs ilyen foglalás.")
    elif valasztas == "3":
        foglalasok = szalloda.foglalasok_listazasa()
        if foglalasok:
            print("Foglalt szobák száma:", len(foglalasok))
            print("Foglalt szobák:", ", ".join(foglalasok))
        else:
            print("Nincsenek foglalások.")
    elif valasztas == "4":
        print("Kilépés...")
        break
    else:
        print("Érvénytelen választás.")
