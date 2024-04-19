# 1. feladat
camps = []
with open("taborok.txt", "r") as f:
    for row in f:
        words = row.strip().split()
        for i in range(4):
            words[i] = int(words[i])
        camps.append(words)

# 2. feladat
print("2. feladat")
print(f"A táborok száma: {len(camps)}")
print(f"Az elsőnek rögzített tábor témája: {camps[0][5]}")
print(f"Az utólsónak rögzített tábor témája: {camps[-1][5]}")
# 3. feladat
print("3. feladat")
music = False
for item in camps:
    if item[-1] == "zenei":
        print(f"Zenei tábor kezdődik {item[0]}. hó {item[1]}. napján.")
        music = True
if not music:
    print("Nem volt zenei tábor")
# 4. feladat
maxParc = [["0"]*6]
for item in camps:
    if len(item[4]) > len(maxParc[0][4]):
        maxParc.clear()
        maxParc.append(item)
    elif len(item[4]) == len(maxParc[0][4]):
        maxParc.append(item)
print("A legnépszerűbb tábor:")
for c in maxParc:
    print(f"Indulás dátuma: {c[0]}.{c[1]}. Tábor témája {c[-1]}")

# 5. feladat
def sorszam(month:int, day: int):
    if month == 6:
        seq = day - 15
    if month == 7:
        seq = 30 - 15 + day
    if month == 8:
        seq = 30 - 15 + 31 + day
    return seq

# 6. feladat
print("6. feladat")
nrMonth = int(input("Adja meg a hónap számát: "))
nrDay = int(input("Adja meg a nap számát: "))
count = 0
for item in camps:
    if sorszam(item[0], item[1]) <= sorszam(nrMonth,nrDay) <= sorszam(item[2], item[3]):
        count +=1

print(f"Ekkor éppen {count} tábor tart.")

# 7. feladat
print("7. feladat")
def sorting (e):
    return sorszam(e[0], e[1])
studnt = input("Adja meg a tanuló betűjelét: ")
studntCamps = []
for item in camps:
    if studnt.upper() in item[-2]:
        studntCamps.append(item)

studntCamps.sort(key=sorting)
canGo = True
for i in range(len(studntCamps) - 1):
    if sorszam(studntCamps[i][2], studntCamps[i][3]) > sorszam(studntCamps[i+1][0], studntCamps[i+1][1]):
        canGo = False

if canGo:
    print("Elmehet mindegyik táborba!")
else:
    print("Nem mehet el mindegyik táborba!")



with open("egytanulo.txt", "w") as f:
    for item in studntCamps:
        f.write(f"{item[0]}.{item[1]}.-{item[2]}.{item[3]}. {item[-1]}\n")