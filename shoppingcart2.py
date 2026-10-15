

foods = []
prices = []
total = 0


while True:
    food = input("kaja (Q kilépéshez)")
    if food.lower() == "q":
        break
    else:
        price = float(input("ár "))
        prices.append(price)
        foods.append(food)

print("-----YOUR CART-----")


for food in foods:
    print(food, end=" ")

for price in prices:
    total += price


print(f"össz: {total}huf")
