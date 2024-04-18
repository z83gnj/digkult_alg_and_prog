adatok=[]
with open("rendel.txt","r")as file:
    for sor in file:
        szavak=sor.strip().split()
        szavak[0]=int(szavak[0])
        szavak[2]=int(szavak[2])
        adatok.append(szavak)

print("2.feladat")
print(f"A rendelések száma: {len(adatok)}")

print("3.feladat")
rendelesek_szama=0
napszam=int(input("Kérem adjon meg egy napot: "))
for i in adatok:
    if i[0]==napszam:
        rendelesek_szama+=1
print(f"A rendelesek száma az adott napon: {rendelesek_szama}")
