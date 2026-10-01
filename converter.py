# a program mértékegység átváltásokat csinál 

valtozo = input("mit akarsz atvaltani")
valtando = input("amibe akarod átváltani")

szam = int(input("írd be az átváltandó számot"))

if valtozo == "cm" and valtando == "dm":
    print(szam / 10)

elif valtando == "m":
    print(szam / 100)

elif valtozo == "dm" and valtando == "cm":
    print(szam * 10)












