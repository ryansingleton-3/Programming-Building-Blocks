
print("Welcome to the roller coaster! Before you are admitted to ride, please answer the following questions.")
first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = int(input("What is the height of the first rider (inches)? "))
second_rider = input("Is there a second rider (yes/no)? ")
if second_rider.lower() == "yes":
    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = int(input("What is the height of the second rider (inches)? "))
    if (first_rider_age >= 18 or second_rider_age >= 18) and first_rider_height >= 36 and second_rider_height >= 36:
        can_ride = True
    elif first_rider_height >= 36 and second_rider_height < 36:
        can_ride = False
    elif first_rider_height < 36 and second_rider_height >= 36:
        can_ride = False
    else:
        can_ride = False

if first_rider_age >= 18 and first_rider_height >= 62 and second_rider.lower() == 'no':
    can_ride = True
else:
    can_ride = False

if first_rider_height < 36:
    can_ride = False


if can_ride:
    print("Congratulations, you may enter. Enjoy the ride!")
else:
    print("Sorry, you are not allowed to ride. Try a smaller and less intense ride.")