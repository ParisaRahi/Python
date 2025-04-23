dato1 = input("Oppgi en dato for både dag og måned i form av et heltall (for eks: 1012): ")
dato2 = input("Oppgi en annen dato for både dag og måned i form av et heltall (for eks: 1012): ")

#konverter string til int for å sammenligne
diff = int(dato1) - int(dato2)

if(diff == 0):
    print("samme dato!")
if(diff > 0):
    print("Feil rekkefølge!")
if(diff < 0):
    print("Riktig rekkefølge!")        




