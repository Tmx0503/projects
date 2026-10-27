import random

def spin_row():
    symbols = ["q", "w", "l", "a", "m"]
    # Visszaadjuk a sorsolt listát, hogy a main() tudja használni
    return random.choices(symbols, k=5)

def print_row(row):
    print(f"\n[{' | '.join(row)}]\n")   # ai help

def get_payout(row, amount):
    symbols = ["q", "w", "l", "a", "m"]

    for word in symbols:
        x = row.count(word)

        if x == 5:
            print("jackpot")
            return amount * 1000
        elif x == 4:
            print("lucky guy")
            return amount * 50
        elif x == 3:
            print("3 word")
            return amount * 5
            
    # Ide csak akkor jut el, ha a fenti ciklusban nem volt nyeremény
    print("not lucky")
    return 0

def main():
    balance = 100
    print("Welcome to losing money!")
    print("Symbols: q, w, l, a, m")
    
    is_running = True  # Egy egyenlőségjel és True, hogy elinduljon a játék
    
    while is_running:
        print(f"\nCurrent balance: {balance}")
        amount = int(input("How much do you want to lose?? "))
        
        # Levonjuk a tétet pörgetés előtt
        balance -= amount
        
        porgetett_sor = spin_row()
        print_row(porgetett_sor)
        
        # Hozzáadjuk az egyenleghez a nyereményt (ha nem nyert, 0-t ad hozzá)
        balance += get_payout(porgetett_sor, amount)
        
        print(f"Remaining balance: {balance}")
        
        # Megkérdezzük, akar-e még játszani
        quit = input("You still want to lose your money? (y/n) ")
        if quit == "n":
            is_running = False

# Biztonsági kapu a futtatáshoz
if __name__ == '__main__':
    main()