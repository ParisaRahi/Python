#del 1
tallListe = [2,5,7]
tallListe.append(11)
print("Første tal:" ,tallListe[0], "\nTredje tall:", tallListe[2])

#del 2
tomListe = []
navn1 = input("Oppgi 4 navn: ")
navnListe = {tomListe.append(navn)for navn in navn1.split()}
#print(tomListe)

#del 3
if len(tomListe) <= 0 and len(tomListe)>4: 
    if "Parisa" in tomListe:
        print("Du husket meg!") 
    else:
        print("Glemte du meg?")
else:
    print("Du burde skrive 4 navn")           

#del 4
sum = 0
for tall in tallListe:
    sum += tall

produkt = 1
for tall in tallListe:
    produkt *= tall

nyListe = [sum , produkt]
sammenslåttListe = tallListe + nyListe
print("sammenslått Liste: " , sammenslåttListe)

sammenslåttListe.pop(-1)
sammenslåttListe.pop(-1)

print("ny sammenslått Liste: " , sammenslåttListe)



