# 1. FELADAT
#   Adatok beolvasása
#   Dict létrehozása a rendelésszámok szortírozásához, és tárolásához
    # NR - Nem volt reklám
    # PL - Plakátreklám volt
    # TV - TV reklám volt.
        # Order - rendelések száma egy napon
        # Pieces - rendelt darabszám egy napon
    # MAX - Maximális rendelt mennyiség
    # MAXDAY - Az első nap ahol a maximális rendelt mennyiség előfordul.
inputdata = { "NR"     : {"Order": [0] * 30, "Pieces" : [0] * 30},
              "PL"     : {"Order": [0] * 30, "Pieces" : [0] * 30},
              "TV"     : {"Order": [0] * 30, "Pieces" : [0] * 30},
              "MAX"    : 0,
              "MAXDAY" : 0}

# Fájl megnyitása, adatok szortírozása
with open("rendel.txt","r") as inputfile:
    for line in inputfile:
        words = line.strip().split()
        day = int(words[0])
        city = words[1].upper()
        piece = int(words[2])
        inputdata[city]["Pieces"][day - 1] += piece
        inputdata[city]["Order"][day - 1 ] += 1

# 5. feladat max rendelés szám, és annak a napja.
        if piece > inputdata["MAX"]:
            inputdata["MAX"] = piece
            inputdata["MAXDAY"] = day
print(f"A rendel.txt fájl beolvasva!")

# 2. FELADAT
#    Rendelések összegzése
print("2. FELADAT")
sum_order=sum(inputdata["NR"]["Order"]) + sum(inputdata["PL"]["Order"]) + sum(inputdata["TV"]["Order"]) 
print("A teljes időszakban leadott összes rendelés: ", sum_order)


# 3. FELADAT
# Rendelések száma adott napon
print("3. FELADAT")
chosenday = input("Kérem adja meg a nap számát (1-30): ")
if chosenday.isdigit():
    chosenday = int(chosenday)
    if 0 < chosenday <= 30:
        sum_dayOrder = inputdata["NR"]["Order"][chosenday - 1] + inputdata["NR"]["Order"][chosenday - 1] + inputdata["NR"]["Order"][chosenday - 1]
        print (f"A {chosenday}. napon leadott rendelések száma: {sum_dayOrder}")
    else:
        print ("HIBA!!! A megadott nap nincs a vizsgált intervallumban!!!")
else:
    print("HIBA!!! Nem számot adott meg!!!")

# 4. FELADAT
# Rendelésmentes napok száma a reklámmal nem érintett városban
print("4. FELADAT")
count = 0
for order in inputdata["NR"]["Order"]:
    if order == 0:
        count += 1
    
if count == 0:
    print ("Minden nap volt rendelés a reklámban nem érintett városból.")
else:
    print (count, " nap nem volt rendelés a reklámban nem érintett városból.")

# 5. FELADAT
# Max rendelési mennyiség, és melyik nap.
# Meghatározása a fájl feldolgozás közben.
print("5. FELADAT")
print(f"A legnagyobb darabszám: {inputdata["MAX"]}, a rendelés napja: {inputdata["MAXDAY"]}")

# 6. FELADAT
# Függvény az adott nap rendeléseinek meghatározására. Paraméterek város kétbetűs kód és a nap és egyébb ha szükséges
def osszes(city:str, day:int, orders:dict):
    city = city.upper()
    if city in list(orders.keys()):
        if 0 < day <= len(orders[city]["Pieces"]):
            return orders[city]["Pieces"][day-1]
        else:
            print(f"A day={day} paraméter nincs a vizsgált intervallumban!!!!")
            return -1
    else:
        print(f"A city={city} városnév nem létezik!!!!")
        return -1

# 7. FELADAT
# 21. nap városokra lebontva a rendelések száma.
print("7. FELADAT")
chosenday = 21
pl = osszes(city = "PL", day = chosenday, orders = inputdata)
tv = osszes(city = "TV", day = chosenday, orders = inputdata)
nr = osszes(city = "NR", day = chosenday, orders = inputdata)

if pl > -1 and tv > -1 and nr > -1:
    print(f"A rendelt termékek darabszáma a {chosenday}. napon: PL: {pl}, TV: {tv}, NR: {nr} ")

# 8. FELADAT
# összegzés városokként a 3 időintervallunban kiírás fájlban és a képernyőre
print("8. FELADAT")
summary = {
    "NR" : [sum(inputdata["NR"]["Order"][0:10]), sum(inputdata["NR"]["Order"][10:20]), sum(inputdata["NR"]["Order"][20:30])],
    "PL" : [sum(inputdata["PL"]["Order"][0:10]), sum(inputdata["PL"]["Order"][10:20]), sum(inputdata["PL"]["Order"][20:30])],
    "TV" : [sum(inputdata["TV"]["Order"][0:10]), sum(inputdata["TV"]["Order"][10:20]), sum(inputdata["TV"]["Order"][20:30])]
}

# A táblázat fejléce
print("{:<10} {:<10} {:<10} {:<10}".format("Napok", "1..10", "11..20", "21..30"))

# A táblázat sorai
for key, value in summary.items():
    print("{:<10} {:<10} {:<10} {:<10}".format(key, value[0], value[1], value[2]))

# Kimeneti fájlnév
outname = "kampany.txt"

# adatok kiíratása fájlba
with open(outname, 'w') as outputfile:
    # A táblázat fejléce
    outputfile.write("{:<10} {:<10} {:<10} {:<10}\n".format("Napok", "1..10", "11..20", "21..30"))
    # A táblázat sorai
    for key, value in summary.items():
        outputfile.write("{:<10} {:<10} {:<10} {:<10}\n".format(key, value[0], value[1], value[2]))
    print(f"Az összegzés kiírva a {outname} fájlba!")
