print("Welcome to the word guessing game!\n")
secret_word = "mosiah"
turn = 0
total_letters = len(secret_word)
hint = '_ ' * total_letters
print(f'Your hint is {hint}.')
guess=None
while guess != secret_word.lower():
    guess = input("\nWhat is your guess? ")
    print("Your hint is: ")
    turn = turn + 1
    for i in range(total_letters):
        letter=guess[i]
        secret_letter=secret_word[i]
        if letter==secret_letter:
            print(letter.upper(), end=' ')
        elif letter in secret_word:
            print(letter.lower(),end=' ')
        else:
            print("_",end=' ')
guess.lower()
print()
print("Congratulations, you got it!")
print(f'It took you {turn} guess(es)')