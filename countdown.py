

import time


my_time = int(input("enter time in s"))

#for x in range(0, my_time):
for x in range(my_time, 0, -1 ):   #backwards
    seconds = x % 60
    mins = int(x / 60) % 60
    hrs = int(x/3600) 
    print(f"{hrs:02}:{mins:02}:{seconds:02}")           # számoljon 0tól bastardig
    time.sleep(1)    # mennyi időt skippeljen



print("bastard")











