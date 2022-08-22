
class Celle:
   # Konstruktør
    def __init__(self):
        self._status = "død"


    # Endre status
    def settDoed(self):
        self._status = "Doed"


    def settLevende(self):
        self._status = "Levende"


    # Hente status
    def erLevende(self):
        if self._status == "Levende":
            return True

        else:
            return False


    def hentStatusTegn(self):
        if self.erLevende():
            return "0"
        return"."


    def __str__(self):
        return self.hentStatusTegn
