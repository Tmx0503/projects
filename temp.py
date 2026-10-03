
unit = input("is this temperature in Celsius or Fahrenheit (c/f)")  

temp = float(input("enter temp"))
if unit is "C":
    temp = round((9 * temp) / 5 +32 , 1)
    print(f"the temp in f is {temp}")
elif unit == "F":
    temp = round((temp-32) * 5 / 9)
    print(f"the temp in c is {temp}")
else:
    print(f"{unit} is invalid")







