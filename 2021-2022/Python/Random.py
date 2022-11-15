import random as r
elso = r.randint(0,10)
masodik = r.randint(0,10)
harmadik = elso + masodik
tipp =input("Mennyi "+ str(elso) + "+" + str(masodik) + "=")
if (int(tipp) == harmadik):
    print("Az igen!")
else:
    print("Hát nem!")
