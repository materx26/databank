v = 0

while v < 9 :
    v+=1
    print(v, end="")
while v > 1:
    v-=1
    print(v, end="")

#3
print("")

x = 0
y=0
while (y < 5):
    print("")
    while (x < 10):
        print("*", end="")
        x+=1
    x = 0
    y+=1

#4
print("")
x = 0
y=0
b=0
while (y < 5):
    print("")
    x = 0
    while (x <= b):
        if (x == b):
            print("*", end="")
        else:
            print(" ", end="")
        x+=1
    
    b+=1
    y+=1

print(" ")
#5
szam1 = 1
sszam1 = 0
szam2 = 1
szum = 0
while szam2 <= 10:
    szam1=sszam1
    while szam1 <= 10:
        szum = szam1 * szam2
        print(str(szam2)+"*"+ str(szam1)+ "="+ str(szum))
        szam1+=1
    sszam1+=1
    szam2+=1
