#validate user input excercise
# username nem több 12 karakternél
# nem tartalmazhat spacet
# nem lehet benne  számok

jelszo = input("írd be a jelszavad  ")
szam_tartalom = jelszo.isdigit()
jelszo_karakter = len(jelszo) #számolja a karakter számot
space = jelszo.count(" ")
#itt írja ha sok a karakter
if jelszo_karakter > 12: 
    print("túl sok karakter")

else:
    print("a jelszó helyes")
if szam_tartalom == False:
    print("helyes")
else:
    print("bastard")
if space > 0:
    print("rossz")
else:
    print("jó")




