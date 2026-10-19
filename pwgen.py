import random
lenght = int(input("milyen hosszú legyen"))

while True:

    if lenght == 0:
        print("ilyen opció nincs")
        lenght = int(input("milyen hosszú legyen"))
    else:
        break
#password = random.randint()
 


character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

for keszlet in range(lenght) :
    print(random.choice(character_string), end="")








#print(password)










