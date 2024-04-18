# 2. feladat
inputData = []
with open("helsinki.txt", "r") as inputFile:
    for row in inputFile:
        words = row.strip().split()
        words[0] = int(words[0])
        words[1] = int(words[1])
        inputData.append(words)

# 3. feladat
print("3. Feladat")
print(f"A pontszerző helyezések száma: {len(inputData)}")

# 4. feladat
print("4. Feladat")
places = [0]*6
for row in inputData:
    places[row[0]-1] += 1

print(f"Aranyérmek száma: {places[0]}")
print(f"Ezüstérmek száma: {places[1]}")
print(f"Bronzérmek száma: {places[2]}")
print(f"Összesen: {sum(places[:3])}")

# 5. feladat
print("5. Feladat")
points = [7,5,4,3,2,1]
sumPoints = sum([place * point for place, point in zip(places, points)])
print(f"Olimpiai pontok száma: {sumPoints}")

# 6. feladat
print("6. feladat")
swimm=0
gym=0

for row in inputData:
    if (row[2] == "uszas") and (row[0] < 4):
        swimm += 1
    elif (row[2] == "torna") and (row[0] < 4):
        gym += 1

if swimm > gym: print("Úszás sportágban szereztek több érmet")
elif swimm < gym: print("Torna sportágban szereztek több érmet")
else: print("Egyenlő volt az érmek száma")

# 7. feladat
with open("helsinki2.txt", "w",encoding='utf-8') as outputFile:
    for row in inputData:
        if row[2] == "kajakkenu":
            row[2] = "kajak-kenu"
        row.insert(2, points[row[0]-1])
        for word in row:
            outputFile.write(str(word)+" ")
        outputFile.write("\n")

# 8. feladat
print("8. feladat")
maxNumber=[0,0,0,0]

for row in inputData:
    if row[1] > maxNumber[1]:
        maxNumber = row.copy()
print(f"Helyezés: {maxNumber[0]}")
print(f"Sportág: {maxNumber[2]}")
print(f"Versenyszám: {maxNumber[3]}")
print(f"Sportolók száma: {maxNumber[1]}")



