# loops Operations
print('--------- for i loop -- iterate 5 times and print anything -----------')
for i in range(5):
    print('Welcome to Python ', i)

print('--------- for i loop -- print numbers from 1 to 10 --- print the numbers horizontally --------')
for i in range(1, 11):
    print(i, end=' ')

print('\n--------- for i loop -- print numbers from 1 to 10  step 2 -------')
for i in range(1, 11, 2):
    print(i, end=' ')

print('\n--- for i loop : Control statements - Continue,   break -------')
print('-- continue ---')
for i in range(1, 11):
    if i in (3, 6):  # range(3, 6)
        continue # skip this iterate [ loop ]
    print(i)

print('-- break ---')
for i in range(1, 11):
    if i == 8:
        break # Exit the Loop
    print(i)


print('\n------------ Nested Loops : Multiplication table ----------------')
for i in range(1, 11): # i = rows
    for j in range(1, 11): # j = columns
        if i * j < 10:
            print(i * j, end='   ')
        else:
            print(i * j, end='  ')
    print('') # \n
