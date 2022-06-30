items = ['Milk', 'Butter', 'Eggs', 'Bread']
new_item = input('Please enter the items of the shopping list (type: quit to finish): ')
for item in items:
    print(f' Item: {item}')

print()

for i in range(len(items)):
    item = items[i]
    print(f' {i + 1}. {item}')