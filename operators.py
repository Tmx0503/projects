# logikus operátorok 
# or = vagy  az eggyiknek igaznak kell lennie 
# and = és mindkettőnek igaznak kell lennie
# not = True-ból False-ot csinál, a False-ból pedig True-t.

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("the outdoor event cancelled")
 
else:
    print("good")



