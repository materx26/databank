def foros():
    for ember in range(3):
        th = float(input(f"Mennyi a(z) {ember+1}. testhőmérséklete? "))
        while th < 34 or th > 45:
            print(f"Ez nem reális hőfok! ({th})")
            th = float(input(f"Mennyi a(z) {ember+1}. testhőmérséklete? "))
        print(f"{ember+1}.")
        if (th < 36):
            print("Enyhe kihülés.")
        elif (th  >= 36 and th  < 37):
            print("Normál!")
        elif (th  >= 37 and th  <= 38):
            print("Hő emelkedés!")
        elif (th  > 38 and th  < 40):
            print("Magas láz!")
        elif (th  > 40):
            print("Kórház!")
def listas():
    hofokok = []
    for _ in range(3):
        th = float(input(f"Mennyi a testhőmérséklete? "))
        while th < 34 or th > 45:
            print(f"Ez nem reális hőfok! ({th})")
            th = float(input(f"Mennyi a testhőmérséklete? "))
        hofokok.append(th)
    for i in range(len(hofokok)):
        print(f"{i+1}.")
        if (hofokok[i] < 36):
            print("Enyhe kihülés.")
        elif (hofokok[i] >= 36 and hofokok[i] < 37):
            print("Normál!")
        elif (hofokok[i] >= 37 and hofokok[i] <= 38):
            print("Hő emelkedés!")
        elif (hofokok[i] > 38 and hofokok[i] <= 40):
            print("Magas láz!")
        elif (hofokok[i] > 40):
            print("Kórház!")
    hofokok.sort()
    for i in range(len(hofokok)):
        print(hofokok[i],end=",")
    print("")
    hofokok.reverse()
    for i in range(len(hofokok)):
        print(hofokok[i],end=",")
    print("")
w = int(input("foros:0 listas:1? "))
if (w == 0):
    foros()
elif(w==1):
    listas()
