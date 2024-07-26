# program to show dictionary operations
print('---- create and print dictionary -----')
shopping_cart_dict = {'Milk': 40.0, 'Eggs': 160.0, 'Bread': 30.0}
print(shopping_cart_dict)
print(type(shopping_cart_dict)) # dict
print(len(shopping_cart_dict)) # 3

print('------ Adding new key | value _____ change value of a key to the dictionary -------')
shopping_cart_dict['Nescafe'] = 60.0    # Adding new key | value
shopping_cart_dict['Milk'] = 45.0       # Change = edit = update the value
print(shopping_cart_dict)

print('------ access element -----')
print('Price of Eggs = ', shopping_cart_dict['Eggs'])
# add 25% to the price of Eggs
shopping_cart_dict['Eggs'] = shopping_cart_dict['Eggs'] + 25/100 * shopping_cart_dict['Eggs']
print(shopping_cart_dict)

print('---- delete element pair from dict using pop ------')
shopping_cart_dict.pop('Bread')
print(shopping_cart_dict)
print('------ Concat Multi dictionaries using update() function ------')
home_cart_dict = {'Meat': 400.0, 'Chicken': 125.0, 'Milk': 60.0}
shopping_cart_dict.update(home_cart_dict)
print(shopping_cart_dict)