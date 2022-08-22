from spillebrett import Spillebrett

def main():
    rad = int(input("skriv inn antallRader: "))
    kolonne = int(input("skriv inn antallKolloner: "))

    brett = Spillebrett(rad, kolonne)
    brett.tegnBrett()

    bruker = ""
    while bruker != 'q':
         bruker = input("trykk på Enter for å gå videre eller skriv inn 'q' for å avslutte programmet. \n\n ")

         if bruker == "":
            brett.oppdatering()
            brett.tegnBrett()

# starte hovedprogrammet
main()
