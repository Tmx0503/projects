
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shipping_label("dr", "idk,", "ize",
               street="fake",
                kake="make" )


#print(f"{kwargs.get('street')}")
#print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")







