# program to show list of dictionaries operations
persons_list = [ {101: 'Omar', 102: 'Esraa', 103: 'Ibrahim'} ]
print(len(persons_list)) # 1 element

# {101: 'Omar', 102: 'Esraa', 103: 'Ibrahim'}
print(persons_list[0])

# Esraa
print(persons_list[0][102])

print('--- Loop over dict keys | values ---')
for key, value in persons_list[0].items():
    print(key)
    print(value)
    print('---')

print('add new dict to the list')
students_dict = {104: 'Esam', 105: 'Ayman', 106: 'Hagar'}
persons_list.append(students_dict)
print(persons_list)

# Ayman
print(persons_list[1][105])