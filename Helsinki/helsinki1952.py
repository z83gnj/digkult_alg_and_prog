print("2.feladat")
adatok=[]
with open("helsinki.txt","r")as file:
    for sor in file:
        szavak=sor.strip().split()
        szavak[0]=int(szavak[0])
        szavak[1]=int(szavak[1])
        adatok.append(szavak)
print("A fájl beolvasása megtörtént")

print("3.feladat")
helyezesek=len(adatok)
print(f"Ponteszerő helyezések száma: {helyezesek}")

print("4.feladat")
helyez=[0]*6
for sor in adatok:
    if sor[0]==1:
        helyez[0]+=1
    elif sor[0]==2:
        helyez[1]+=1
    elif sor[0]==3:
        helyez[2]+=1
    elif sor[0]==4:
        helyez[3]+=1
    elif sor[0]==5:
        helyez[4]+=1
    elif sor[0]==6:
        helyez[5]+=1
print(f"Arany: {helyez[0]}")
print(f"Ezüst: {helyez[1]}")
print(f"Bronz: {helyez[2]}")
print(f"Összesen: {helyez[0]+helyez[1]+helyez[2]}")

print("5.feladat")
osszpont=helyez[0]*7+helyez[1]*5+helyez[2]*4+helyez[3]*3+helyez[4]*2+helyez[5]*1
print(f"Olimpiai pontok száma: {osszpont}")
##pont=[7,5,4,3,2,1]
##osszpont1=0
##for i in range(6):
##    osszpont1+=helyez[i]*pont[i]
##print(osszpont1)

print("6.feladat")
uszas=0
torna=0
for sor in adatok:
    if (sor[2]=="uszas") and (sor[0]<=3):
        uszas+=1
    elif (sor[2]=="torna") and (sor[0]<=3):
        torna+=1
if uszas>torna:
    print("Úszása sportágban szereztek több érmet")
elif torna>uszas:
    print("Torna sportágban szereztek több érmet")
else:
    print("Egyenlő volt az érmek száma")

print("8.feladat")
maxsportolo=[0,0,0,0]
for sor in adatok:
    if sor[1]>maxsportolo[1]:
        maxsportolo=sor.copy()

print(f"Helyezes: {maxsportolo[0]}")
print(f"Sportág: {maxsportolo[2]}")
print(f"Versenyszám: {maxsportolo[3]}")
print(f"Sportolók száma: {maxsportolo[1]}")










