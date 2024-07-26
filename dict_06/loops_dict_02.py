# how to loop over a dictionary
# Lists, Tuples    for i loop index | for each
# dictionary [ only use For each Loop ]  as there is NO INDEX in the dictionary
shopping_cart_dict = {'Milk': 40.0, 'Eggs': 160.0, 'Bread': 30.0}

print('---- 1. Loop over a dictionary KEYS using for each Loop ----')
for key in shopping_cart_dict:
    print(key)
    print(shopping_cart_dict[key]) # value
    print('---')

print('---- 2. Loop over a dictionary KEYS | values using for each Loop')
for key, value in shopping_cart_dict.items():
    print(key)
    print(value)
    print('---')
