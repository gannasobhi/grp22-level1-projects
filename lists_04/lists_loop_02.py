
my_list = [14, 7, 9, 2, 3, 10]

print('---- 1. loop over the list using for i loop = we use the index ------')
total = 0
for i in range( len(my_list) ):
    print( my_list[i] )
    total = total + my_list[i]

print('total of the numbers = ', total)

print('-------- 2. Loops over the List using For each Loop [for in loop ] --- Do not use index')
total = 0 # reset the variable
for item in my_list:
    print(item)
    total = total + item

print('total of the numbers = ', total)

print('--- 3.  using the builtin function sum() -----')
print(sum(my_list))