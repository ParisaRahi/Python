import random
from celle import Celle

class Spillebrett:

    def __init__(self, antallRader, antallKolonner):

       self._rader = antallRader
       self._kolonner = antallKolonner
       self._generasjon = 0
       self._rutenett = []

       for rad in range(self._rader):
           celler = []
           for kolonne in range(self._kolonner):
               celler.append(Celle())
           self._rutenett.append(celler)
       self._generer()


    def _generer(self):
        for rad in range(self._rader):
             for kolonne in range(self._kolonner):
                tilfeldigAntallCelle = random.randint(0,2)
                if tilfeldigAntallCelle == 0:
                    self._rutenett[rad][kolonne].settLevende()


    def tegnBrett(self):

        for rad in range(self._rader):
            for celle in range(self._kolonner):
                print(self._rutenett[rad][celle].hentStatusTegn(), end ="" )
            print()
            print()
        print("generasjonAntall", self._generasjon)
        print("AntallLevende: ",str(self.finnAntallLevende()))

    def finnNabo(self,antallRader,antallKolonner):
        naboListe = []

        for i in range(-1,2):
            for j in range(-1,2):
                naboRad = antallRader + i
                naboCelle = antallKolonner + j

                gyldig = True

                if i == 0 and j == 0:
                    gyldig = False

                if naboRad < 0 or naboRad >= self._rader:
                    gyldig = False

                if naboCelle < 0 or naboCelle >= self._kolonner:
                    gyldig = False

                if gyldig:
                   naboListe.append(self._rutenett[naboRad][naboCelle])

        return naboListe

    def oppdatering(self):
        doedeCeller = []
        levendeCeller = []

        for i in range(self._rader):
            for j in range(self._kolonner):
                # j.erLevende()
                naboer = self.finnNabo(i, j)

                levendeNaboer = 0
                for nabo in naboer :
                    if nabo.erLevende():
                        levendeNaboer += 1

                if self._rutenett[i][j].erLevende():
                    if levendeNaboer < 2 or levendeNaboer > 3:
                        doedeCeller.append(self._rutenett[i][j])

                    if levendeNaboer == 2 or levendeNaboer == 3:
                        levendeCeller.append(self._rutenett[i][j])


                else:
                    if levendeNaboer == 3 :
                        levendeCeller.append(self._rutenett[i][j])

        for en in doedeCeller:
            en.settDoed()

        for en in levendeCeller:
            en.settLevende()

        self._generasjon += 1

    def finnAntallLevende(self):
        levendeCeller = 0
        for rad in self._rutenett:
            for celle in rad:
                if celle.erLevende():
                    levendeCeller += 1

        return levendeCeller
