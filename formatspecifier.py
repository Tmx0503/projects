# formátumspecifikálók = {:jelzők} egy értéket formáz a beillesztett
#                                jelzők (flags) alapján

# .(szám)f = kerekítés ennyi tizedesjegyre (fixpontos)
# :(szám) = ennyi karakterhely lefoglalása
# :03 = ennyi karakterhely lefoglalása és feltöltése nullákkal
# :< = balra igazítás
# :> = jobbra igazítás
# :^ = középre igazítás
# :+ = pluszjel használata a pozitív értékek jelölésére
# := = a előjel elhelyezése a legbaloldalibb pozícióba
# :  = egy szóköz beszúrása a pozitív számok elé
# :, = ezreselválasztó vessző

price1 = 3.14159
price2 = -987.65
price3 = 12.34
#print(f"price 1 {price1:11}") 11 space van a szám előtt
#print(f"price 1 {price1:011}") a szám előtt van 11 nulla
#print(f"price 1 {price1:<11}") utána van a 11 space ha meg így van > akkor olyan mint a line 18
#print(f"price 1 {price1:+}")  plusz tesz eléjük
#print(f"price 1 {price1:,}") ezres szeparáló




print(f"price 1 {price1:.2f}")
print(f"price 2 {price2:>5}")
print(f"price 3 {price3}")



