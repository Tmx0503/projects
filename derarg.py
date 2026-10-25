

#flexible

# def arguments szóval ha a () ban a value után = jelet teszel akkor az defa értéke lesz neki

def net_price(list_price, disc=0, tax=0.05): # ezért csak a price kell a (ba)
    return list_price * (1-disc) * (1 + tax)




