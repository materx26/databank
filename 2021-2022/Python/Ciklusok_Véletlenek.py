import random as r

gondolt_szam = r.randint(1,6)
print(gondolt_szam)

megvan = False
proba = 3
while not megvan and proba > 0:
    proba -= 1
    szam = int(input("Írj egy számot!"))
    if (szam == gondolt_szam):
        print("Ügyes!")
        megvan = True
    elif (proba > 0):
        print("Újra!")
    elif (proba <= 0):
        print("Viszlát!")
