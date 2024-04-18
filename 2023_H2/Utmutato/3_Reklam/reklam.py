def fel1():
    print("1. feladat:")
    with open("rendel.txt", 'r') as rendfile:
        rendelesek = []
        for line in rendfile:
            nap, varos, darab = line.split()
            rendelesek.append({'nap': int(nap), 'varos': varos, 'darab': int(darab)})
    return rendelesek

def fel2(rendelesek):
    print("2. feladat:")
    print("A rendelések száma:", len(rendelesek))

def fel3(rendelesek):
    print("3. feladat:")
    nap = int(input("Kérem adjon meg egy napot: "))
    rendszam = sum(1 for rend in rendelesek if rend['nap'] == nap)
    print("A rendelések száma az adott napon:", rendszam)

def fel4(rendelesek):
    print("4. feladat:")
    nap = 1
    nemvolt = 0
    for rend in rendelesek:
        if rend['varos'] == "NR" and rend['nap'] != nap:
            nemvolt += rend['nap'] - nap - 1
            nap = rend['nap']
    nemvolt += 30 - nap
    if nemvolt > 0:
        print(nemvolt, "nap nem volt a reklámban nem érintett városból rendelés")
    else:
        print("Minden nap volt rendelés a reklámban nem érintett városból")

def fel5(rendelesek):
    print("5. feladat:")
    maxrend = max(rendelesek, key=lambda rend: rend['darab'])
    print("A legnagyobb darabszám:", maxrend['darab'], ", a rendelés napja:", maxrend['nap'])

def osszes(rendelesek, varos, nap):
    ossz = sum(rend['darab'] for rend in rendelesek if rend['varos'] == varos and rend['nap'] == nap)
    return ossz

def fel7(rendelesek):
    print("7. feladat:")
    plossz = osszes(rendelesek, "PL", 21)
    tvossz = osszes(rendelesek, "TV", 21)
    nrossz = osszes(rendelesek, "NR", 21)
    print("A rendelt termékek darabszáma a 21. napon PL:", plossz, "TV:", tvossz, "NR:", nrossz)

def fel8(rendelesek):
    print("8. feladat:")
    varosok = ["PL", "TV", "NR"]
    ossztiz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for rend in rendelesek:
        naptiz = (rend['nap'] - 1) // 10
        vartiz = varosok.index(rend['varos'])
        ossztiz[vartiz][naptiz] += 1

    with open("kampany.txt", 'w') as kampfile:
        kampfile.write("Napok\t1..10\t11..20\t21..30\n")
        for vartiz in range(len(varosok)):
            kampfile.write(varosok[vartiz])
            for naptiz in range(3):
                kampfile.write('\t' + str(ossztiz[vartiz][naptiz]))
            kampfile.write('\n')

def main():
    rendelesek = fel1()
    fel2(rendelesek)
    fel3(rendelesek)
    fel4(rendelesek)
    fel5(rendelesek)
    fel7(rendelesek)
    fel8(rendelesek)

if __name__ == "__main__":
    main()
