


import time 
def count(start, end):   # ha def értéket akarsz ebben az esetben (a másodiknak kell lennie)

    for x in range(start, end+1):
        print(x)
        time.sleep(1)

    print("done")

count(0, 10)


