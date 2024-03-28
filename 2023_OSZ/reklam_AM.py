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

# print (nr)
# print (pl) 
# print (tv) 

# 2. Össz rendelés szám meghatározása.
print("2. feladat:")
print("Az összes leadott rendelések száma: ", sum(nr) + sum(pl) + sum(tv))


# 3. Adott napon hány rendelés történt
print ("3. feladat:")

input


try:
    # Try to cast the variable to an integer
    result = int(variable)
    print("Casting successful. Result:", result)
except ValueError:
    # Handle the case where casting fails
    print("Casting failed. The variable is not a valid integer.")