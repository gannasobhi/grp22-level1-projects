# program to check for person age
# inputs مدخلات البرنامج

person_age = input('PLease enter a no : ')
# convert from string to int  [  casting  ]
person_age = int(person_age)

# processing = equation  المعادلات
# output result
if person_age > 16:
    print('You are a man')
# elif person_age >= 11 and person_age <= 16:
elif person_age >= 11:
    print('You are a boy')
else:
    print('you are a child')

