import random


lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("The game")
print(f"select a num between {lowest_num} and {highest_num}")

while is_running:

    guess = input("enter your guess ")


    if guess.isdigit():
        guess = int(guess)
        guesses += 1
    

        if guess > highest_num or guess < lowest_num:
            print("bastartd")
            print(f"select a num between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("too low")
        elif guess > answer:
             print("too much") 
        else:
             print("correct!!")     
             print(f"nums of guesses : {guesses}")
             is_running = False  
                   
            
    else:
            print("bastard")
            print(f"select a num between {lowest_num} and {highest_num}")
    







