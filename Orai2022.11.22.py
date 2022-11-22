ev = [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305,2650,]
ev_b = False
if (len(ev) == 12):
    ev_b = True
    print(f"ez egy év adatsora")
else:
    print(f"ez nem egy év adatsora!")
ln = ev[0]
for szam in ev:
    if szam > ln:
        ln = szam
print(f"A legnagyobb: {ln}")
lk = ev[0]
for szam in ev:
    if szam < lk:
        lk = szam
print(f"A legkisebb: {lk}")
ossz = 0
for szam in ev:
    ossz += szam
print(f"Összesen: {ossz}")
#2400 alatt
ker = 2400
menny = 0
for szam in ev:
    if (szam < 2400):
        menny += 1
print(f"{menny} hónapban volt 2400 alatt.")
i = 0
while i < len(ev) and ev[i] != ln:
    i+=1
print(f"A legnagyobb a(z) {i+1}. helyen van!")
i = 0
while i < len(ev) and ev[i] != lk:
    i+=1
print(f"A legkisebb a(z) {i+1}. helyen van!")
