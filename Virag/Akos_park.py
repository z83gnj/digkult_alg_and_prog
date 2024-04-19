#1. feladat
offers = []
with open("felajanlas.txt", "r") as f:
    for row in f:
        words = row.strip().split()
        if len(words) == 1:
            nrBed = int(words[0])
        else:
            words[0] = int(words[0])
            words[1] = int(words[1])
            offers.append(words)

flowerBeds = ["#"] * nrBed
winner = [0] * nrBed

#2. feladat
print("2. feladat")
print(f"A felajánlások száma: {len(offers)}")

#3. feladat
print("3. feladat")
count = 1
boothSide = ""
for item in offers:
    if item[0] > item[1]:
        boothSide += str(count)+" "
    count +=1

print(f"A bejárat mindkét oldalára ültetők: {boothSide}")

#4. feladat
print("4. feladat")
count = 1
for item in offers:
    if item[0] < item[1]:
        for i in range(item[0] - 1, item[1]):
            if flowerBeds[i] == "#":
                flowerBeds[i] = item[2]
                winner[i] = count
            else:
                flowerBeds[i] += item[2]
    else:
         for i in range(item[0]-1, nrBed):
            if flowerBeds[i] == "#":
                flowerBeds[i] = item[2]
                winner[i] = count
            else:
                flowerBeds[i] += item[2]
         for i in range(0, item[1]):
            if flowerBeds[i] == "#":
                flowerBeds[i] = item[2]
                winner[i] = count
            else:
                flowerBeds[i] += item[2]
    count +=1

nrOfBed = int(input("Adja meg az ágyások sorszámát: "))
if flowerBeds[nrOfBed] != "#":
    print(f"A felajánlások száma: {len(flowerBeds[nrOfBed])}")
    print(f"A virágágyás színe ha csak az első ültethet: \"{flowerBeds[nrOfBed][0]}\"")
    print(f"A virágágyás színei: {" ".join(set(flowerBeds[nrOfBed]))}")
else:
    print("Ezt az ágyást nem ültették be!")

#5. feladat
print("5. feladat")
sumOffer = 0
if "#" not in flowerBeds:
    print("Minden ágyás beültetésére van jelentkező!")
else:
    for item in flowerBeds:
        if item[0] != "#":
            sumOffer += len(item)
    if sumOffer >= nrBed:
        print("Átszervezéssel megoldható az ültetés!")
    else:
        print("A beültetés nem oldható meg!")

#6. feladat
with open("szinek.txt", "w") as f:
    for b, w in zip(flowerBeds,winner):
        f.write(f"{b[0]} {w}\n")
