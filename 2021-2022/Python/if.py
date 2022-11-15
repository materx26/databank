import random as r
gondolt_szam = r.randint(1, 5)
print("Súgó: ", gondolt_szam)
print("Gondoltam egy számra!")
tipp = input("Tippelj ")
tipp = int(tipp)
if (tipp == gondolt_szam ):
    print("Ügyes!")
    print("Grat")
elif (tipp == gondolt_szam+1 or tipp == gondolt_szam-1):
    print("Majdnem!")
else:
    print("Nem talált!")
    print("Ne" + 120 * "e")
print("Viszlát!")
