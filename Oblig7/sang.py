class Sang:

    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist 


    def spill(self):
        print(f"Nå spilles {self._tittel} med {self._artist}")


    def sjekk_artist(self, navn):
        artistNavnListe = self._artist.split()
        oppgittNavnListe = navn.split()

        for artist in oppgittNavnListe:
            navn = artist.lower()
            for n in artistNavnListe:
                nyttNavn = n.lower()
                if navn == nyttNavn:
                    return True            
        return False  


    def sjekk_tittel(self, tittel):
        if tittel.lower() == self._tittel.lower():
            return True
        return False



    def sjekk_artist_og_tittel(self, artist, tittel):
        if self.sjekk_tittel(tittel) and self.sjekk_artist(artist):
            return True
        return False

        

    def streng_til_fil(self):
        streng = self._tittel + ";" + self._artist + "\n"
        return streng
        
    

    def __str__(self):
        return f"{self._tittel}"




       
