fel_szam = int(input("Kérek egy számot! "))
next_fel_szam = fel_szam
szum1 = 0
szum2 = 0

while (szum1 <= 5):
    szum2 = 0
    
    if (szum1 == 1):
        print(fel_szam, end=" ")
        while (szum2 < 4):
            next_fel_szam+=1
            print(next_fel_szam, end=" ")
            szum2+=1
    if (szum1 > 1):
        print("")
        while (szum2 < 5):
            next_fel_szam+=1
            print(next_fel_szam, end=" ")
            szum2+=1
    szum1+=1
