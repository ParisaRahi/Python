from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn


    def lesFraFil(self, filNavn):
        sangInfo = open("musikk.txt","r")
        for linje in sangInfo:
            alleData = linje.strip().split(";")
            self._sanger.append(Sang(alleData[0], alleData[1]))
        sangInfo.close()


    def leggTilSang(self, nySang):
            self._sanger.append(nySang)

    def fjernSang(self, sang):
            self._sanger.remove(sang)


    def spillSang(self, sang):
            sang.spill()


    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()
        return self

    def finnSang(self, tittel):
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang
        return None

    def hentArtistUtvalg(self, artistNavn):
        minListe = []
        for sanger in self._sanger:
            if sanger.sjekkArtist(artistNavn):
                minListe.append(sanger)
        return minListe
