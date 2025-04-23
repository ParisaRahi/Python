# 2.skriver ut "Hei Student i terminalen"
print("Hei student!")

# 3.ber brukren å oppgi navn ved hjelpe av input()-> returnere tekststreng
#så lagrer inputet og printer ut "Hei navn"
fornavn = input("Skriv navnet ditt: ")
print("Hei" , fornavn)

# 4.oppretter to heltallvariabler og printe dem ut
lengde = 35
bredde = 42
print("Lengde er: ", lengde)
print("Bredde er: ", bredde)
#Alternativ
print("Lengde er: ", lengde, "\nBredde er: ", bredde)

# 5.differanse av lengde og bredde
diff = lengde - bredde
print("Differanse: ",diff)

#6. oppgi nytt navn , oppretter en variabel som sammen og printe den ut
etternavn = input("Skriv etternavnet ditt: ")
sammen = fornavn + etternavn
print("Sammen er: ", sammen)

#7. legger til "og" sammen med mellomrom mellom de to navnene
sammen = fornavn + " og " + etternavn
print("Nysammen er: ", sammen)


