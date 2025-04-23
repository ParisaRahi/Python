from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn


    def les_fra_fil(self):
        fil = open(self._navn + ".txt", "r")
        for linje in fil:
            alle_data = linje.strip().split(";")
            tittel = alle_data[0]
            artist = alle_data[1]
            self._sanger.append(Sang(tittel, artist))
        fil.close()    


    def legg_til_sang(self, ny_sang):
        self._sanger.append(ny_sang)


    def fjern_sang(self, sang):
        self._sanger.remove(sang)


    def spill_alle(self):
        for sang in self._sanger:
            sang.spill()


    def finn_sang_tittel(self, tittel):
        for sang in self._sanger:
            if sang.sjekk_tittel(tittel):
                return sang
        return None 


    def hent_artist_utvalg(self, artistnavn):
        sangListe = []
        for sang in self._sanger:
            if sang.sjekk_artist(artistnavn):
                sangListe.append(sang)
        return sangListe


    def skriv_til_fil(self):
        fil = open(self._navn + ".txt", "w")
        for sang in self._sanger:
            fil.write(sang.streng_til_fil())
            print(sang)
            
        fil.close()


    def __str__(self):
        streng = f"Spillelisten {self._navn} spilles av med sangene i listen:\n"
        for sang in self._sanger:
            streng += sang + "\n"
        return streng






