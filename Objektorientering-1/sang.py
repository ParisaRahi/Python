class Sang:

    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist

    def spill(self):
        print("Spill", self._tittel, "Av", self._artist)

    def sjekkArtist(self, artistNavn):
        artisListe = self._artist.split()
        artistliste2 = artistNavn.split()

        for navn in artisListe:
            if navn in artistliste2 :
                return True

        return False

    def sjekkTittel(self, tittelNavn):

            if tittelNavn.lower() == self._tittel.lower():
                return True
            return False

    def sjekkArtistOgTittel(self, artistNavn, tittelNavn):
        if self.sjekkTittel(tittelNavn) and self.sjekkArtist(artistNavn):
            return True
        return False

    def __str__(self):
        return f"{self._tittel} av {self._artist}"
