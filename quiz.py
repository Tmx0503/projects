
questions = ("How many elements are in the periodic table?:",
             "Which animal lays the largest eggs?:",
             "What is the most abundant gas in Earth's atmosphere?:",
             "How many bones are in the human body?:",
             "Which planet in the solar system is the hottest?:")

options = (("A. ", "B. ", "C. ", "D. "),
           ("A. ", "B. ", "C. ", "D. "),
           ("A. ", "B. ", "C. ", "D. "),
           ("A. ", "B. ", "C. ", "D. "),
           ("A. ", "B. ", "C. ", "D. "))

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("enter (a,b,c,d)").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("wrong")    
    question_num += 1

print("results")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(score)



