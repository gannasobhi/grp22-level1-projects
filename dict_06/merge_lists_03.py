# program to merge 2 lists into a dictionary
emp_ids_list = [101, 102, 103]
emp_names_list = ['Ahmed', 'Omar', 'Sarah']

# create empty dictionary
persons_dict = {}

# Loop over emp_ids_list using for i index loop
for i in range(len(emp_ids_list)):
    # print(i, emp_ids_list[i], emp_names_list[i])
    persons_dict[ emp_ids_list[i] ] = emp_names_list[i]  # Fill [ add items to dict ]

print(persons_dict)