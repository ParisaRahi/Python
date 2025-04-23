vareOrdbok = {"melk" : 14.90, "brød": 24.90 , "yoghurt": 12.90, "pizza": 39.90}
print(vareOrdbok)
for i in range(2):
    vare1 = input("skriv en vare med sine priser (vare : pris)")
    vare = vare1.split(":")
    key = vare[0]
    value = vare[1]
    vareOrdbok[key] = value

print("skriver ut ordboken på nytt: ", vareOrdbok)