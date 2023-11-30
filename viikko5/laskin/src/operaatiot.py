
class Summa:
    def __init__(self, logiikka, syote):
        self._logiikka = logiikka
        self._syote = syote

    def suorita(self):
        self._logiikka.plus(self._syote())

class Erotus:
    def __init__(self, logiikka, syote):
        self._logiikka = logiikka
        self._syote = syote

    def suorita(self):
        self._logiikka.miinus(self._syote())

class Nollaus:
    def __init__(self, logiikka):
        self._logiikka = logiikka

    def suorita(self):
        self._logiikka.nollaa()

class Kumoa:
    def __init__(self, logiikka):
        self._logiikka = logiikka

    def suorita(self):
        self._logiikka.kumoa()
