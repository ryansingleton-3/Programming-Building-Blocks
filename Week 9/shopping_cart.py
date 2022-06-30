import math

print("Welcome to the Shopping Cart Program!")
action = 0
products = []
prices = []
new_product = ''
price = float()
sum = 0



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
        new_price = float(input(f'What is the price of {new_product}? '))
        rewards = input('Are you a rewards member (yes or no)?: ')
        if rewards.lower() == 'yes':
            new_price = new_price * 0.90
            prices.append(new_price)
            print(f'Congratulations, you get a 10% discount. Your new price for {new_product} is ${new_price:.2f}.')
        else:
            prices.append(new_price)
        print(f"'{new_product}' has been added to the cart.")
        print()
    elif action == "2":
        print()
        print("Your shopping cart:")
        for i in range(len(products)):
            product = products[i]
            price = prices[i]
            print(f'{i + 1}. {product} - ${price:.2f}') # need to make this only show 2 decimal places
        print()
    elif action == "3":
        removed_item = int(input("Which item would you like to remove? "))
        removed_item = removed_item - 1
        products.pop(removed_item)
        prices.pop(removed_item)
        print('Item removed')
        print()
    elif action == "4":
        for j in range(0, len(prices)):
            sum = sum + prices[i]
        print(f'The total price of the items in the shopping cart is ${sum:.2f}')
        print()
    elif action == "5":
        print("Thank you. Have a great day!")
        print()
