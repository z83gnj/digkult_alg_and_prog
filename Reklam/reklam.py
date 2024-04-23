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
napszam=9
#napszam=int(input("Kérem adjon meg egy napot: "))
for i in adatok:
    if i[0]==napszam:
        rendelesek_szama+=1
print(f"A rendelesek száma az adott napon: {rendelesek_szama}")

print("4.feladat")
nap=1
szamlalo=30
for i in adatok:
    if i[0]>nap:
        nap+=1
    if i[1]=="NR" and i[0]==nap:
        nap+=1
        szamlalo-=1
if szamlalo==0:
    print("Minden nap volt rendelés a reklámban nem érintett városból")
else:
    print(f"{szamlalo} nap nem volt a reklámban nem érintett városból rendelés")

print("5.feladat")
max_rendeles=0
max_nap=0
for i in adatok:
    if i[2]>max_rendeles:
        max_rendeles=i[2]
        max_nap=i[0]
print(f"A legnagyobb darabszám: {max_rendeles}, a rendelés napja: {max_nap}")
    
def osszes(varos:str,nap:int):
    rendelt_termekek=0
    for i in adatok:
        if i[1]==varos and i[0]==nap:
            rendelt_termekek+=i[2]
    return  rendelt_termekek
    
    

print(osszes("TV",12))

