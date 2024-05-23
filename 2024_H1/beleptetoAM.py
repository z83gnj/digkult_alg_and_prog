inpuData = []
with open("bedat.txt") as f:
    for line in f:
        words = line.strip().split()
        words[1] = words[1].split(":")
        words[1][0] = int(words[1][0])
        words[1][1] = int(words[1][1])
        words[2] = int(words[2])
        inpuData.append(words)

print("2.feladat")

print(f"Az első tanuló {inpuData[0][1][0]:02}:{inpuData[0][1][1]:02}-kor lépett be a főkapun.")
print(f"Az utolsó tanuló {inpuData[-1][1][0]:02}:{inpuData[-1][1][1]:02}-kor lépett ki a főkapun.")

print("\n3.feladat")
idostart = 7 * 60 + 50
idoend = 8 * 60 + 15
with open("kesok.txt", "w") as f:
    for item in inpuData:
        if idostart < item[1][0] * 60 + item[1][1] <= idoend:
            f.write(f"{item[1][0]}:{item[1][1]} {item[0]}\n")
print("kesok.txt elkészült")

print("\n4.feladat")
menza = 0
konyvtar = set()
for item in inpuData:
    if item[2] == 3:
        menza += 1
    elif item[2] == 4:
        konyvtar.add(item[0])
print(f"A menzán aznap {menza} tanuló ebédelt.")

print("\n5.feladat")
print(f"Aznap {len(konyvtar)} tanuló kölcsönzött a könyvtárban.")
if len(konyvtar) > menza:
    print("Többen voltak, mint a menzán ")
else:
    print("Nem voltak többen, mint a menzán")

print("\n6.feladat")
szunetStart = 10 * 60 + 45
kapuZar = 10 * 60 + 50
szunetVege = 11 * 60
szunetBelep = {}

for item in inpuData:
    if kapuZar < item[1][0] * 60 + item[1][1] <= szunetVege and item[2] == 1:
        szunetBelep[item[0]] = 0

for item in inpuData:
    if kapuZar > item[1][0] * 60 + item[1][1] and item[0] in szunetBelep.keys():
        if item[2] == 1:
            szunetBelep[item[0]] += 1
        elif item[2] == 2:
            szunetBelep[item[0]] -= 1

diakok = ""
for key, item in szunetBelep.items():
    if item != 0:
        diakok += key + " "

print(f"Az érintett tanulól:\n{diakok}")

print("\n7.feladat")
azonosito = input("Egy tanuló azonosítója: ")
#azonosito = "zoom"
elsobe = False
for item in inpuData:
    if item[0] == azonosito.upper():
        if item[2] == 1 and not elsobe:
            beido = item[1][0] * 60 + item[1][1]
            elsobe = True
        elif item[2] == 2:
            kiido = item[1][0] * 60 + item[1][1]
print(f"A tabnuló érkezése és távozása között {int((kiido - beido) / 60)} óra {(kiido - beido) % 60} perc telt el.")

