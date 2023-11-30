class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edelliset_arvot = []

    def miinus(self, operandi):
        self._edelliset_arvot.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._edelliset_arvot.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def kumoa(self):
        _edellinen = self._edelliset_arvot.pop()
        if _edellinen is not None:
            self._arvo = _edellinen

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def hae_edellinen(self):
        return self._edelliset_arvot.pop()

    def tarkista_edellinen(self):
        return bool(len(self._edelliset_arvot) > 0)
