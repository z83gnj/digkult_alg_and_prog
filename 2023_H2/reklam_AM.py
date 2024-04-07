# 6. összesítő függvény készítése
def osszes(city, day):
    print("test")

# 1. Adatok beolvasása

# Listák a rendelések számához.
# nr - Nem volt reklám
# pl - Plakátreklám volt
# tv - TV reklám volt.
nr = [0] * 30
pl = [0] * 30
tv = [0] * 30

# Bemeneti fájl neve
inputname = "rendel.txt"
max = 0
maxday = 0

# Fájl megnyitása, adatok szortírozása
with open(inputname,'r') as file:
    for line in file:
        words = line.strip().split()
        day = int(words[0]) - 1 
        city = words[1].upper()
        order = int(words[2])
        if city == "NR":
            nr[day] = nr[day] + order
        elif city == "PL":
            pl[day] = pl[day] + order
        elif city == "TV":
            tv[day] = tv[day] + order
 # 5. feladat max rendelés szám, és annak a napja.
        if order > max:
            max = order
            maxday = day       


# print (nr)
# print (pl) 
# print (tv) 

# 2. Össz rendelés szám meghatározása.
print("2. feladat:")
print("Az összes leadott rendelések száma: ", sum(nr) + sum(pl) + sum(tv))

# 3. Adott napon hány rendelés történt
print ("3. feladat:")
day = input("Kérem adjon meg a nap számát(1-30): ")
# Ellenőrzés hogy a megadott szám megfelelő-e
if day.isdigit():
    day = int(day)
    if 0 < day <=30:    
        print("Az adott napot ", nr[day] + pl[day] + tv[day], "rendelés történt." )
    else:
        print("A megadott napszám nem esik a vizsgált intervallumba!!!")
else:
    print("A megadott érték nem szám!!!")

# 4. Hány nap nam volt rendelés a reklámmal nem érintett városban.
print("4. feladat")
count = 0
for order in nr:
    if order == 0:
        count += 1

if count == 0:
    print ("Minden nap volt rendelés a reklámban nem érintett városból.")
else:
    print (count, " nap nem volt rendelés a relkában nem érintett városból.")

# 5. feladat max rendelés szám, és annak a napja.
print("A legnagyobb darabszám: ", max, ", a rendelés napja: ", maxday)