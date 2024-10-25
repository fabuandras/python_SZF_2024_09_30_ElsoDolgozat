import math

# 1. feladat:
print("1. feladat: ")

nev1 = input("Kérem az első nevet: ")
nev2 = input("Kérem a második nevet: ")

jegy1 = int(input(f"Kérem {nev1} jegyét: "))
jegy2 = int(input(f"Kérem {nev2} jegyét: "))

print(f"{nev1} jegye: {jegy1}, {nev2} jegye: {jegy2} programozásból.")


# 2. feladat:
print("2. feladat: ")

x = float(input("Kérem az első valós számot (x koordináta): "))
y = float(input("Kérem a második valós számot (y koordináta): "))
sugar = float(input("Kérem a sugár értékét: "))

# pont = ()

# if pont < sugar:
#     print("A pont a körön belül van.")
# elif pont == sugar:
#     print("A pont rajta van a körön.")
# elif pont > sugar:
#     print("A pont a körön kívül van.")


# 3. feladat:
print("3. feladat: ")

szam1 = int(input("Kérem az első egész számot: "))
szam2 = int(input("Kérem a második egész számot: "))

if ((-9 <= szam1 <= 9) and szam1 % 2 == 0) or ((-9 <= szam2 <= 9) and szam2 % 2 == 0):
    print("Van köztük egyjegyű és páros szám.")
elif (szam1 < 0 and szam1 % 2 != 0) and (szam2 < 0 and szam2 % 2 != 0):
    print("Mindkét szám negatív és páratlan szám.")
else:
    print("Egyik kategóriába sem illik.")


# 4. feladat:
print("4. feladat: ")

nap = input("Kérem a nap nevét (pl. Hétfő): ")
ora = input("Kérem az óra nevét (pl. programozás): ")

if nap == "Hétfő" and ora == "programozás":
    print("Misi hétfőn dolgozik a programozás órán.")
elif nap == "Kedd":
    print("Misi kedden alszik az összes órán.")
elif nap == "Szerda" and ora == "programozás":
    print("Misi programozás órán van és nem dolgozik.")
elif nap == "Csütörtök":
    print("Misi csütörtökön minden órán figyel, mert jó kedve van (aznap szokott moziba menni).")
elif nap == "Péntek":
    print("Misi pénteken a hétvégéről ábrándozik, így csak félig figyel minden aznapi órán.")
else:
    print("Nem tudjuk, mit csinál Misi az adott órán ezen a napon.")
