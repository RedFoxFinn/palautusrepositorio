OLETUSARVO = 5

class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def _tarkista_arvo(self, asetettava_arvo):
        if asetettava_arvo is None:
            return False
        elif not isinstance(asetettava_arvo, int) or asetettava_arvo < 0:
            return False
        else:
            return True

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti if self._tarkista_arvo(kapasiteetti) else OLETUSARVO
        self.kasvatuskoko = kasvatuskoko if self._tarkista_arvo(kasvatuskoko) else OLETUSARVO

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, arvo):
        on = 0

        for indeksi in range(0, self.alkioiden_lkm):
            if arvo == self.ljono[indeksi]:
                on = on + 1

        if on > 0:
            return True
        else:
            return False

    def lisaa(self, arvo):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = arvo
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        else:
            pass

        if not self.kuuluu(arvo):
            self.ljono[self.alkioiden_lkm] = arvo
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_lista(self.ljono, taulukko_old)
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)

            return True

        return False

    def poista(self, arvo):
        kohta = -1
        apu = 0

        for indeksi in range(0, self.alkioiden_lkm):
            if arvo == self.ljono[indeksi]:
                kohta = indeksi  # siis luku löytyy tuosta kohdasta :D
                self.ljono[kohta] = 0
                break

        if kohta != -1:
            for indeksi in range(kohta, self.alkioiden_lkm - 1):
                apu = self.ljono[indeksi]
                self.ljono[indeksi] = self.ljono[indeksi + 1]
                self.ljono[indeksi + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, vanha_lista, uusi_lista):
        for indeksi in range(0, len(vanha_lista)):
            uusi_lista[indeksi] = vanha_lista[indeksi]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for indeksi in range(0, len(taulu)):
            taulu[indeksi] = self.ljono[indeksi]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a_arvo,b_arvo in zip(a_taulu, b_taulu):
            x.lisaa(a_arvo)
            x.lisaa(b_arvo)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
