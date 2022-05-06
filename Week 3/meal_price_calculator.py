

child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_of_children = int(input('How many children are there? '))
number_of_adults = int(input('How many adults are there? '))
tax_rate = int(input('What is the sales tax rate? '))
print()
subtotal = float(round(((child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)),2))
sales_tax = float((subtotal * tax_rate / 100))
total = float(round((subtotal + sales_tax),2))
print(f'Subtotal: ${round(subtotal, 2)}')
print(f'Sales Tax: ${round(sales_tax, 2)}')
print(f'Total: ${total}')
print()
payment_amount = float(input('What is the payment amount? '))
change = float(payment_amount - total)
print(f'${round(change, 2)} is your change.')
tip_percentage = float(input('What percentage of the total would you like to tip? '))
tip_amount = (total * tip_percentage) / 100
print(f'With a {tip_percentage}% tip, that will equal ${round(tip_amount, 2)}.')
print('Thank you for your business, and your generous tip.')



