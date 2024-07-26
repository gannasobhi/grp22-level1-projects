# The program is to generate another list,
# which contains only unique elements and another which contains the duplicate elements

# inputs  المدخلات
my_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]


# operations المعادلات
unique_list = []
duplicates_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
    elif item not in duplicates_list:
        duplicates_list.append(item)

# Output النتائج
print('Unique List = ', unique_list)
print('Duplicated List = ', duplicates_list)