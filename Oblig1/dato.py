dato1 = input("Oppgi en dato for både dag og måned i form av heltall(for eks 12 og 24 for 12.desember):")
dag1 = int(dato1[0:2])
maned1 = int(dato1[6:8])

dato2 = input("oppgi en anne dato for både dag og måned i form av heltall (for eks 06 og 10 for 06.oktober):")
dag2 = int(dato2[0:2])
maned2 = int(dato2[6:8])

if (maned1 == maned2):
    if(dag1 < dag2):
        print("Riktig rekkefølge!")
    elif(dag1 > dag2):
        print("Feil rekkefølge!")
    else:
        print("Samme dato!")
elif(maned1 < maned2):
    if(dag1 < dag2):
        print("Riktig rekkefølge!")
    elif(dag1 > dag2):
        print("Feil rekkefølge!")
elif(maned1 > maned2):
    print("Feil rekkefølge")



