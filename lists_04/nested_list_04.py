# program to show nested list operations
my_list = [
            [101, 'Ahmed', 'Cairo'],
            [102, 'Omar', 'Alex'],
            [103, 'Ibrahim', ['Cairo', 'Nasr city', 'Abbas El Akkad']]
          ]

print(my_list)
# print the first element [101, 'ahmed', 'cairo']
print(my_list[0])

# print Alex
print(my_list[1][2] )

# print Nasr city
print(my_list[2][2][1])

# add this list to my_list
new_person = [104, 'Amir', 'Gharbeya']
my_list.append(new_person)
# my_list.extend(new_person)
print(my_list)



