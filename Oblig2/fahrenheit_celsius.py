#del 1 -> definere en variabel for fahrenheit
fahrenheit = 90

#del 2 -> printe variabelen ut
print("Temperaturen i fahrenheit er: " , fahrenheit)

#del 3 -> definere en variabel for celsius og regne den ut fra fahrenheit
celsius = (fahrenheit - 32) * 5/9

#del 4 -> printe ut variabelen celsius
print("Temperaturen i celsius er: " , "%.2f" %celsius)

#del5 -> får fahrenheit fra brukeren og konvertere den til celsius
fahrenheitFraBrukeren = int(input("Skriv temperturen i fahrenheit: "))
print("oppgitt temperaturen i fahrenheit er: " , fahrenheitFraBrukeren)
konvertereTilCelsiusn= (fahrenheitFraBrukeren - 32) * 5/9
print("Temperaturen i celsius er: " , "%.2f" %konvertereTilCelsiusn)
