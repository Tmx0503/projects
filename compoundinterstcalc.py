

principle = 0
rate = 0
time = 0


while principle <= 0:
    principle = float(input("enter the principal amount"))
    if principle <= 0:
        print("wrong")

while rate <= 0:
    rate = float(input("enter the interest"))
    if rate <= 0:
        print("wrong")

while time <= 0: #while True is lehetne de akkor kell else: break alá
    time = int(input("enter the time"))
    if time <= 0:
        print("wrong")


total = principle * pow((1 + rate / 100), time)

print("total")









