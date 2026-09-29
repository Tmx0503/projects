import math

muvelet = (input("milyen műveletet akarsz"))
    
szam_1 = int(input("írd be a számot"))
szam_2 = int(input("írd be a számot"))

if muvelet == "+":
    print(szam_1 + szam_2)

elif muvelet == "-":
    print(szam_1 - szam_2)

elif muvelet == "*":
    print(szam_1 * szam_2)

else:
    print(szam_1 / szam_2)



