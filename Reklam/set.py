def pontszam(szam:int):
    if szam<50:
        jegy=1
    elif 50<=szam<60:
        jegy=2
    elif 60<=szam<70:
        jegy=3
    elif 70<=szam<85:
        jegy=4
    elif szam>85:
        jegy=5
    return [szam,jegy]

def osztalyzat(pont:int):
    if pont<50:
        return [pont,1]
    elif 50<=pont<60:
        return [pont,2]
    elif 60<=pont<70:
        return [pont,3]
    elif 70<=pont<85:
        return [pont,4]
    elif pont>85:
        return [pont,5]


a=int(input("Adj meg egy számot: "))
jegy=pontszam(a)
print(pontszam(a))
print(osztalyzat(a))
jegy2=osztalyzat(


        
