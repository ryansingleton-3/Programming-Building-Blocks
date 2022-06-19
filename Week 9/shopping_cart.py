print("Welcome to the Shopping Cart Program!")
action = 0
products = []
prices = []
new_product = ''



print()

# print("1. Add Item")
# print("2. View Cart")
# print("3. Remove Item")
# print("4. Compute Total")
# print("5. Quit")
# action = input("Please enter an action: ")

while action != "5":
    print("Please select one of the following:")
    print()
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute Total")
    print("5. Quit")
    action = input("Please enter an action: ")
    if action == "1":
        new_product = input('What item would you like to add? ')
        products.append(new_product)
        print(f'{new_product} has been added to the cart.')
        print()
    elif action == "2":
        print()
        print("Your shopping cart:")
        for product in products:
            print(product)
        print()
    elif action == "3":
        print("Sorry, I haven't gotten to this part yet.")
        print()
    elif action == "4":
        print("Sorry, I haven't gotten to this part yet.")
        print()
    elif action == "5":
        print("Thank you. Have a great day!")
        print()