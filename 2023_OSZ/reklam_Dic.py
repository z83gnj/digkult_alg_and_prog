# 1. FELADAT
#   Adatok beolvasása
def fileread(inputname:str):
# dict létrehozása a rendelésszámok szortírozásához, és tárolásához
    # NR - Nem volt reklám
    # PL - Plakátreklám volt
    # TV - TV reklám volt.
    # MAX - Maximális rendelt mennyiség
    # MAXDAY - Az első nap ahol a maximális rendelt mennyiség előfordul.
    inputdata = { "NR"     : [0] * 30,
                  "PL"     : [0] * 30,
                  "TV"     : [0] * 30,
                  "MAX"    : 0,
                  "MAXDAY" : 0}

    # Fájl megnyitása, adatok szortírozása
    with open(inputname,'r') as file:
        for line in file:
            words = line.strip().split()
            day = int(words[0]) - 1 
            city = words[1].upper()
            order = int(words[2])
            inputdata[city][day] += order

    # 5. feladat max rendelés szám, és annak a napja.
            if order > inputdata["MAX"]:
                inputdata["MAX"] = order
                inputdata["MAXDAY"] = day 

    return inputdata   

# 2. FELADAT
#   Rendelések összegzése
def summorders(orders:dict):
    print("2. FELADAT")
    ordersum = sum(orders["NR"]) + sum(orders["PL"]) + sum(orders["TV"])
    print("A teljes időszakban leadott összes rendelés: ", ordersum)

# 3. FELADAT
# Rendelések száma adott napon
def orderAtDay(orders:dict):
    print("3. FELADAT")
    chosenday = input("Kérem adja meg a nap számát (1-30): ")
    if chosenday.isdigit():
        chosenday = int(chosenday)
        if 0 < chosenday <= 30:
            ordersum = orders["NR"][chosenday] + orders["PL"][chosenday] + orders["TV"][chosenday]
            print (f"A {chosenday}. napon leadott rendelések száma: {ordersum}")
        else:
            print ("HIBA!!! A megadott nap nincs a vizsgált intervallumban!!!")
    else:
        print("HIBA!!! Nem számot adott meg!!!")

# 4. FELADAT
# Rendelésmentes napok száma a reklámmal nem érintett városban
def checkNoOrder(cityorders:list):
    print("4. FELADAT")
    count = 0
    for order in cityorders:
        if order == 0:
            count += 1
    
    if count == 0:
        print ("Minden nap volt rendelés a reklámban nem érintett városból.")
    else:
        print (count, " nap nem volt rendelés a relkában nem érintett városból.")

# 5. FELADAT
# Max rendelési mennyiség, és melyik nap.
# Meghatározása a fájl feldolgozás közben.
def maxOrder(max:int, maxday:int):
    print("5. FELADAT")
    print(f"A legnagyobb darabszám: {max}, a rendelés napja: {maxday}")

# # 6. FELADAT
# # Függvény az adott nap rendeléseinek meghatározására. Paraméterek város kétbetűs kód és a nap.
def osszes(city:str, day:int):
    print("test")


allorders = fileread("rendel.txt")
summorders(allorders)
orderAtDay(allorders)
checkNoOrder(allorders["NR"])
maxOrder(allorders["MAX"], allorders["MAXDAY"])