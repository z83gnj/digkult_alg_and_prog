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
    with open(inputname,'r') as inputfile:
        for line in inputfile:
            words = line.strip().split()
            day = int(words[0]) - 1 
            city = words[1].upper()
            order = int(words[2])
            inputdata[city][day] += order

    # 5. feladat max rendelés szám, és annak a napja.
            if order > inputdata["MAX"]:
                inputdata["MAX"] = order
                inputdata["MAXDAY"] = day 
    print(f"A {inputname} fájl beolvasva!")
    return inputdata   

allorders = fileread("rendel.txt")
print("A következő városazonosítók lette beolvasva:")
count = 1
for key in list(allorders.keys())[:3]:
    print (key)

# 2. FELADAT
#   Rendelések összegzése
print("2. FELADAT")
ordersum = sum(allorders["NR"]) + sum(allorders["PL"]) + sum(allorders["TV"])
print("A teljes időszakban leadott összes rendelés: ", ordersum)

# 3. FELADAT
# Rendelések száma adott napon
print("3. FELADAT")
chosenday = input("Kérem adja meg a nap számát (1-30): ")
if chosenday.isdigit():
    chosenday = int(chosenday)
    if 0 < chosenday <= 30:
        ordersum = allorders["NR"][chosenday] + allorders["PL"][chosenday] + allorders["TV"][chosenday]
        print (f"A {chosenday}. napon leadott rendelések száma: {ordersum}")
    else:
        print ("HIBA!!! A megadott nap nincs a vizsgált intervallumban!!!")
else:
    print("HIBA!!! Nem számot adott meg!!!")

# 4. FELADAT
# Rendelésmentes napok száma a reklámmal nem érintett városban
print("4. FELADAT")
count = 0
for order in allorders["NR"]:
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
print(f"A legnagyobb darabszám: {allorders["MAX"]}, a rendelés napja: {allorders["MAXDAY"]}")

# 6. FELADAT
# Függvény az adott nap rendeléseinek meghatározására. Paraméterek város kétbetűs kód és a nap és egyébb ha szükséges
def osszes(city:str, day:int, orders:dict):
    city = city.upper()
    if city in list(orders.keys()):
        if 0 < day <= len(orders[city]):
            return orders[city][day-1]
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
pl = osszes(city = "PL", day = chosenday, orders = allorders)
tv = osszes(city = "TV", day = chosenday, orders = allorders)
nr = osszes(city = "NR", day = chosenday, orders = allorders)

if pl > -1 and tv > -1 and nr > -1:
    print(f"A rendelt termékek darabszáma a {chosenday}. napon: PL: {pl}, TV: {tv}, NR: {nr} ")

# 8. FELADAT
# összegzés városokként a 3 időintervallunban kiírás fájlban és a képernyőre
print("8. FELADAT")
summary = {
    "NR" : [sum(allorders["NR"][0:9]), sum(allorders["NR"][10:19]), sum(allorders["NR"][20:29])],
    "PL" : [sum(allorders["PL"][0:9]), sum(allorders["PL"][10:19]), sum(allorders["PL"][20:29])],
    "TV" : [sum(allorders["TV"][0:9]), sum(allorders["TV"][10:19]), sum(allorders["TV"][20:29])]
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