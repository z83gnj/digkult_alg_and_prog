taborok=[]
with  open("taborok.txt","r") as file:
    for sor in file:
        szavak=sor.strip().split()
        szavak[0]=int(szavak[0])
        szavak[1]=int(szavak[1])
        szavak[2]=int(szavak[2])
        szavak[3]=int(szavak[3])
        taborok.append(szavak)
print("2.feladat")
print(f"Az adatsorok száma: {len(taborok)}")
print(f"Az először rögzített tábor témája: {taborok[0][5]}")
print(f"Az utoljára rögzített tábor témája: {taborok[-1][5]}")

print("3.feladat")
for i in taborok:
    if i[5]=="zenei":
        print(f"Zenei tábor kezdődik {i[0]}. hó {i[1]}. napján.")

print("4.feladat")

    

print("5.feladat")
def sorszam(honap:int,nap:int):
        if honap==6:
            szam=nap-15
        if honap==7:
            szam=30-15+nap
        if honap==8:
            szam=30+31-15+nap
        return szam
print("6.feladat")
honap=int(input("hó: "))
nap=int(input("nap: "))
szamlalo=0
for i in taborok:
    if sorszam(i[0], i[1])<= sorszam(honap,nap)<=sorszam(i[2],i[3]):
            szamlalo+=1
print(f"Ekkor éppen {szamlalo} tábor tart.")

print("7.feladat")

            
