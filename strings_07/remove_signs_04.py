# program to Remove all special characters except letters and numbers

statement = 'egypt,@#2024 ..'

new_statement = ''

for letter in statement:
    if letter.isalnum():
        new_statement = new_statement + letter

print(new_statement)
statement = new_statement
print(statement)
