


capitals = {"usa": "washington ",
            "india": "new delhi",
            "china": "beijing",
            "russia": "moscow"}



print(capitals.get("usa")) # így kapom meg a fővárost hogy .get() ugye "usa": "és ami itt van "


if capitals.get("japan"):
    print("létezik")
else:
    print("nem létezik")

capitals.update({"germany": "berlin"})
capitals.pop() # az töröl

keys = capitals.keys()

for key in capitals.keys():
    print(key)

values = capitals.keys()

for value in capital.values():
    print(value)
print(values)

items = capitals.items()       # kidobja a dictet 2d listaként

for key in capital.items():
    print(f"{key}: {value}")


