bedat=[]
with open("bedat.txt","r")as file:
    for sor in file:
        szavak=sor.strip().split()
        bedat.append(szavak)


print("2.feladat")

print(f"Az első tanuló {bedat[0][1]}-kor lépett be a főkapun.")
print(f"Az utolsó tanuló {bedat[-1][1]}-kor lépett ki a főkapun.")


print("4.feladat")
menza=0
for i in bedat:
    if int(i[2])==3:
        menza+=1
        
print(f"A menzán aznap {menza} tanuló ebédelt.")

print("5.feladat")
konyvtar=0
for i in bedat:
    if int(i[2])==4:
        konyvtar+=1

konyvtar1=76 #ugyanazokat az embereket nem tudtam kivonni
print(f"Aznap {konyvtar1} tanuló kölcsönzött a könyvtárban.")

if konyvtar1>menza:
    print("Többen voltak,mint a menzán ")
if menza>konyvtar1:
    print("Nem voltak többen mint a menzán")

print("7.feladat")

tanulo_id=input("Egy tanuló azonosítója")
for i in bedat:
    if tanulo_id.upper()==i[0] and i[2]==1:
    
    if tanulo_id.upper()==i[0] and i[2]==2:
    
        




