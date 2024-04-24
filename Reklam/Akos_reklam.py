# 1. Feladat
inputData=[]
with open("rendel.txt", "r") as f:
    for row in f:
        words = row.strip().split()
        words[0] = int(words[0])
        words[2] = int(words[2])
        inputData.append(words)

# 2. Feladat
print("2. feladat")
print(f"A rendelések száma: {len(inputData)}")

# 3. Feladat
print("\n3. feladat")
orderDay = int(input("Kérem, adjon meg egy napot! "))
count = 0
for item in inputData:
    if item[0] == orderDay:
        count += 1
print(f"A(z) {orderDay}. napon a rendelések száma: {count}")

# 4. Feladat
# A rendelést tartalmazó napok számán alapul
print("\n4. feladat")
count = 30
day = 1
for item in inputData:
    if item[0] > day:
        day += 1
    if (item[1] == "NR") and (item[0] == day):
        day += 1
        count -= 1
if count == 0:
    print("Minden nap volt rendelés a reklámban nem érintett városból")
else:
    print(f"{count} nap nem volt rendelés a reklámban nem érintett városból")

days = set()
for item in inputData:
    if item[1] == 'NR':
        days.add(item[0])
count2 = 30 - len(days)
if count2:
    print(f'{count2} nap nem volt a reklámban nem érintett városból rendelés')
else:
    print('Minden nap volt rendelés a reklámban nem érintett városból')



# A rendelést nem tartalmazó napok számán alapul
nr = [0]*30
for item in inputData:
    if item[1] == "NR":
        nr[item[0]-1] +=1
count1 = nr.count(0)
if count1 == 0:
    print("Minden nap volt rendelés a reklámban nem érintett városból")
else:
    print(f"{count1} nap nem volt rendelés a reklámban nem érintett városból")


# 5. Feladat
print("\n5. feladat")
maxOrder = [0,0]
for item in inputData:
    if item[2] > maxOrder[0]:
        maxOrder[0] = item[2]
        maxOrder[1] = item[0]
print(f"A legnagyobb leadott darabszám: {maxOrder[0]}, a rendelés napja: {maxOrder[1]}")

# 6. Feladat
def osszes(city:str, day:int, orders:list):
    sumOrders = 0
    for item in orders:
        if (item[1] == city.upper()) and (item[0] == day):
            sumOrders += item[2] 
    return sumOrders

# 7. Feladat
print("\n7. feladat")
orderDay = 21

print(f"A rendelt termékek száma a {orderDay}. napon:")
for c in ["PL", "TV", "NR"]:
    print(f"{c}: {osszes(c, orderDay, inputData)}")

# 8. Feladat
print("\n8. feladat")
sumPieces = {
    "PL" : [0, 0, 0],
    "TV" : [0, 0, 0],
    "NR" : [0, 0, 0]}

for item in inputData:
    if item[0] < 11:
        sumPieces[item[1]][0] += 1
    elif item[0] < 21:
        sumPieces[item[1]][1] += 1
    else:
        sumPieces[item[1]][2] += 1
header = ["Napok", "1..10", "11..20", "21..30"]
print(f"{header[0]:<10}{header[1]:<10}{header[2]:<10}{header[3]:<10}")
for key, value in sumPieces.items():
    print(f"{key:<10}{value[0]:<10}{value[1]:<10}{value[2]:<10}")

with open("kampany.txt", "w") as f:
    f.write(f"{header[0]:<10}{header[1]:<10}{header[2]:<10}{header[3]:<10}\n")
    for key, value in sumPieces.items():
        f.write(f"{key:<10}{value[0]:<10}{value[1]:<10}{value[2]:<10}\n")