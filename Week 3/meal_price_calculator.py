

child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_of_children = int(input('How many children are there? '))
number_of_adults = int(input('How many adults are there? '))
tax_rate = int(input('What is the sales tax rate? '))
print()
subtotal = float((child_meal_price * number_of_children) + (adult_meal_price * number_of_adults))
sales_tax = float((subtotal * tax_rate / 100))
total = float((subtotal + sales_tax))
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}')
print()
payment_amount = float(input('What is the payment amount? '))
change = float(payment_amount - total)
print(f'${change:.2f} is your change.')
tip_percentage = float(input('What percentage of the total would you like to tip? '))
tip_amount = (total * tip_percentage) / 100
print(f'With a {tip_percentage}% tip, that will equal ${tip_amount:.2f}.')
print('Thank you for your business, and your generous tip.')



