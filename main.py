questions = (
    "How many days are there in a leap year?",
    "How many legs does a spider have?",
    "Which planet is known as the Red Planet?",
    "What color do you get when you mix red and yellow?",
    "Which animal is known as the King of the Jungle?",
)

answers = (
    ["A: 365", "B: 360", "C: 366", "D: 364"],
    ["A: 6", "B: 8", "C: 4", "D: 10"],
    ["A: EARTH", "B: VENUS", "C: MARS", "D: JUPITER"],
    ["A: GREEN", "B: ORANGE", "C: PURPLE", "D: PINK"],
    ["A: TIGER", "B: ELEPHANT", "C: LION", "D: BEAR"]
)

correct_answers = [
    "C","B","C","B","C"
]
guesses = []
question_index = 0
score = 0
while True:
    for i in range(len(questions)):
        print("--------------------")
        print(questions[i])
        for option in answers[i]:
            print(option)

        guess = input("Enter your answer (A/B/C/D): ").upper()
        guesses.append(guess)

        if guess == correct_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print(f"Your score is {score}")
    print("Correct answers are: ", correct_answers)
    print("Your answers are:", guesses)

    again_or_stop = input("A-Start Again B-Stop: ").upper()
    if again_or_stop == "A":
        continue  
    else:
        break