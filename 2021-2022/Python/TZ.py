szinek = ["kék", "zöld", "piros", "sárga", "zöld", "kék"]
print(", ".join(szinek))
szinek.append(input("Adj meg Te is egy színt! "))
print(", ".join(szinek))
k_szin = input("Milyen színre vagy kíváncsi? ")
num = 0
for szin in szinek:
    if (szin == k_szin):
        num+=1
if (num > 0):    
    print("Van már " + k_szin + " szín a listában,",num,"darab.")
if (num <= 0):
    print("Nincs ilyen szín!")

for index in range(30):
    print("*",end="")
print("")
szin_n = 0
num = 0
megvolt = []
for index in range(len(szinek)):
    num = 0
    for szine in megvolt:
        if (szinek[szin_n] == szine):
            szin_n+=1
    for szin in range(len(szinek)):
        if (szinek[szin_n] == szinek[szin]):
            num+=1
    print(szinek[szin_n] + " :",num)
    szin_n+=1
    megvolt.append(szinek[szin_n])
##atlag = kek + zold + piros + sarga
##atlag = atlag/4
##print("Átlagosan",atlag, "alkalommal szerepelnek a színek a listában.")
