import random
number = random.randint(1,10)
print(number)

guess = -1
turn = 0
last_question = "yes"
while last_question.lower() == "yes":
    magic_number = number = random.randint(1,100)
    while guess != magic_number:  
        guess = int(input("What is your guess? "))
        turn = turn +1
        if guess < magic_number:
            print("higher")
        elif guess > magic_number:
            print("lower")
        else:
            print("You guessed it!")
            print(f'It took you {turn} turns to guess it correctly.')
            last_question = input("Do you want to play again? (yes/no) ")
            if last_question.lower() == "no":
                print("Thank you for playing! Have a great day.")






