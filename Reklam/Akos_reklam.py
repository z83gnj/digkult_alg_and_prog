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
print("3. feladat")
orderDay = int(input("Kérem, adjon meg egy napot! "))
count = 0
for item in inputData:
    if item[0] == orderDay:
        count += 1
print(f"A(z) {orderDay}. napon a rendelések száma: {count}")

# 4. Feladat
print("4. feladat")
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

# 5. Feladat
print("5. feladat")
maxOrder = [0,0]
for item in inputData:
    if item[2] > maxOrder[0]:
        maxOrder[0] = item[2]
        maxOrder[1] = item[0]
print(f"A legnagyobb leadott darabszám: {maxOrder[0]}, a rendelés napja: {maxOrder[1]}")

# 6. Feladat
# 7. Feladat
# 8. Feladat

