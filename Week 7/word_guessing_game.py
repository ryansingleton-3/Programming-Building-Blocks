print("Welcome to the word guessing game!")
print()
secret_word = "mosiah"
turn = 1
guess = input("What is your guess? ")
while guess.lower() != "mosiah":
    turn = turn +1
    print("Your guess was not correct.") 
    guess = input("What is your guess? ")
print("Congratulations! You guessed it!")
print(f'It took you {turn} guesses. ')