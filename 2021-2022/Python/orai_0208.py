
##órai

for szam in range(1,11):
    print(szam, szam**2)

#2
for t in range(3):
    print("")
    for s in range(5):
        for o in range(s):
            print("o", end="")
        print("")


#3

##autok = ["BMW", "Audi", "Opel", "Lada"]
##
##while len(autok)>0:
##    print("Autók:", ", ".join(autok))
##    autot = input("Melyik autót kölcsönzi ki? ")
##    if (autot in autok):
##        autok.remove(autot)
##    else:
##        print("Nincs ilyen autó.")

#Szorgalmi
szamok = []
import random as r
rszam = r.randint(11,20)
first = 0
jo = False
helyes = 0
while first < 10:
    jo = False
    if (rszam in szamok):
        rszam = r.randint(11,20)
    elif(rszam not in szamok):
        print(rszam, "(",rszam**2,")")
        szamok.append(rszam)
        while jo != True:
            meszam = int(input("Mennyi a négyzete? "))
            if (meszam == rszam**2):
                helyes+=1
                jo = True
            else:
                jo = True
        first+=1
print("10-ből ", helyes, "lett jó!")

