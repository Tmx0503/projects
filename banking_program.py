

def show_balance(balance):
    print(f"your balance is {balance:.2f}")


def deposit():
    amount = int(input("enter the money amount"))


    if amount < 0:
        print("bastard")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter the amount"))
    if amount > balance:
        print("no")
        return 0
    elif amount < 0:
        print(" no")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking program")
        print("1.show balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. exit")


        choice = input("enter choice")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("bastard")


    print("say bye bye to your money ")


main()