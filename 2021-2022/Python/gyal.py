import random as r
filmek = ["Mátrix", "Forráskód", "A viharsziget", "Tőrbe ejtve", "Film"]
szerplok = ["Neo", "Brian", "A viharsziget-Név1", "Harlen", "Film-Név2"]
a = 4
def main(a):
    if (a > 0):
        
        num = 0
        for film in filmek:
            print(num,film, end=" ")
            num+=1
        szer_num = r.randint(0,a)
        print("")
        print(szerplok[szer_num])
        inputsz = int(input("Melyik filmben szerpel? (szám): "))
        if (inputsz == szer_num):
            print("Jó!")
        else:
            print("Nemtalált!")
        szerplok.remove(szerplok[szer_num])
        filmek.remove(filmek[szer_num])
        a-=1
        main(a)
main(a)
