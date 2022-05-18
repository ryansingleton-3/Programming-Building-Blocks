grade=int(input("What is your grade percentage? "))
print()
if grade >=90: 
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70: 
    letter = "C"
elif grade >= 60:
    letter = "D"    
elif grade < 60:
    letter = "F"
    print(f'Your grade is: {letter}')
print()
if grade >= 70: 
    print("Congratulations, you passed the class!")
else:
    print("Sorry, you did not pass the class.")
