from sang import Sang
from spilleliste import Spilleliste

def hovedprogram():
    mine_spillelister = {}

    spilleListe_musikk = Spilleliste("musikk")
    spilleListe_musikk.les_fra_fil()
    mine_spillelister["musikk"] = spilleListe_musikk

    spilleListe_queen = Spilleliste("queen")
    artistNavnetQueenList = spilleListe_musikk.hent_artist_utvalg("Queen")
    for sang in artistNavnetQueenList:
        spilleListe_queen.legg_til_sang(sang)
    mine_spillelister["queen"] = spilleListe_queen

    spilleListe_mittValg = Spilleliste("mittValg")
    sang1 = Sang("unstoppable", "Sia")
    sang2 = Sang("titanium", "Sia")
    sang3 = Sang("diamonds", "Rihanna")
    spilleListe_mittValg.legg_til_sang(sang1)
    spilleListe_mittValg.legg_til_sang(sang2)
    spilleListe_mittValg.legg_til_sang(sang3)
    mine_spillelister["mittValg"] = spilleListe_mittValg

    for spilleListe in mine_spillelister.keys():
        if spilleListe == "mittValg":
            mine_spillelister[spilleListe].spill_alle()

    for spilleListe in mine_spillelister.values():
        spilleListe.skriv_til_fil()        




        






    

hovedprogram()