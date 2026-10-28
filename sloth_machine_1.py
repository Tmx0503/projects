import random
def spin_row():
    symbols = ['q', 'w', 'l', 'a' , 'c']
    results = []

    for symbol in range(3):
        results.append(random.choice(symbols))
    return results
def print_row(row):
    print(" ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == 'q':
            return bet * 3
        elif row[0] == 'w':
            return bet * 4 
        elif row[0] == 'c':
            return bet * 5
        elif row[0] == 'l':
            return bet * 10
        elif row[0] == 'a':
            return bet * 50
    return 0

def main():
    balance = 100




    print("welcome to losing money")
    print("symbols: q, w, l, a ,m")
    while balance > 0:
        print(f"your {balance} balance")
        bet = input("place bet")
        if not bet.isdigit():
            print("idiot")
            continue
        bet = int(bet)

        if bet > balance:
            print("poor")
            continue
        if bet <= 0:
            print("többet")
            continue

        balance -= bet
        row = spin_row()
        print("spinning......")
        print_row(row)







        payout = get_payout(row, bet)
        if payout > 0:
            print(f"{payout}")
        else:
            print("soryy you lost this round")

        balance -= payout
        playagain = input("do you want to spin again (y/n)")
        if playagain != 'y':
            break
if __name__ == '__main__':
    main()




































