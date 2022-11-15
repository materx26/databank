import random as r
szam = 0
x = 0
nagyobb = 0
print("A sorsolt számok:")
print("")
while (x < 10):
    szam = r.randint(1, 100)
    if (szam > 50):
        nagyobb+=1
    print(szam, end=" ")
    x+=1
print("")
print(nagyobb, "db nagyobb közülük 50-nél.")
