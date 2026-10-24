import random
guesses = 0
options = ("rock", "paper", "scissors" )
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("enter your choice").lower()

    print(f"player choice:{player}, computer choice. {computer}")

    if player == computer:
        print("It's a tie!")
        guesses += 1
        
    elif player == "rock" and computer == "scissors":
        print("You win!")
        
    elif player == "paper" and computer == "rock":
        print("You win!")
        
    elif player == "scissors" and computer == "paper":
        print("You win!")
        
    else:
        print("You lose!")
        guesses += 1


    
    print(f"your guesses num: {guesses}")
    guesses = 0
    play_again = input("play again (y/n)").lower()
    if not play_again == "y":
        running = False










