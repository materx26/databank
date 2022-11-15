#1
varosok=["Budapest","London","Bécs","Róma","Prága"]
for index in range(len(varosok)):
    print(index, varosok[index])
#2
varosok=["Budapest","London","Bécs","Róma","Prága"]
for index, varos in enumerate(varosok):
    print(index, varos)
#3
import random as r
dobasok = []
for _ in range(10):
    dob = r.choice(["f", "i"])
    dobasok.append(dob)
print(", ".join(dobasok), ".", sep="")
faf=0
for index, dobas in enumerate(dobasok):
    if (index > 0 and dobas == "f" and dobasok[index-1]=="f"):
        faf+=1
print("fej után fej:",faf)
#4
