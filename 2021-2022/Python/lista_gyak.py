##lista = ["Jakus Máté",2006,"december",26,"férfi"]
##print(lista)
##print(lista[0])
##print(lista[3])
##print(lista[:4])
##print(lista[2:])
##print(lista[2:4])
##print(lista[-1])
##
##2
##kacatok = []
##kilep = False
###Változó érték nélkül : kacat = None
##while kilep == False:
##    szavak = input("Kérek egy kacatot! ")
##    if (szavak == "elfogyott"):
##        kilep = True
##    if (szavak != "elfogyott"): 
##        kacatok.append(szavak)
##print("A kacatjaim: ", ", ".join(kacatok), ".", sep="")
##
###3
##italok = ["tea", "víz", "szörp", "pálinka"]
##
##for ital in italok:
##    print("A", ital, "folyékony.")
##
##4

versenyzok = []
versenyzo = None
while versenyzo != "":
    print("A versenyzok jelenleg: ", ", ".join(versenyzok))
    versenyzo = input("Kérek egy versenyzőt! ")
    if (versenyzo != ""):
        versenyzok.append(versenyzo)
print("Az első helyezett: ", versenyzok[0])
print("A második helyezett: ", versenyzok[1])
print("A harmadik helyezett: ", versenyzok[2])
print("Az utolsó helyezett: ", versenyzok[-1])
