#del 1 -> kommunisere med bruekren og printe ut det 
navn = input("Skriv inn navn: ")
bosted = input("Hvor kommer du fra? ")
print("Hei," + navn + "!" + " Du er fra "+ bosted)

#del 2 -> får lest inn informasjon inn i en prosedyre
def hilsen():
    print()
    navn = input("Skriv inn navn: ")
    bosted = input("Hvor kommer du fra? ")
    print("Hei," + navn + "!" + " Du er fra "+ bosted)

hilsen()
hilsen()
hilsen()
