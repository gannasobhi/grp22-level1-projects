 # program to Swap commas and dots in a String

statement = 'He is Ahmed, Ahmed lives in cairo, Ahmed plays football.'

statement = statement.replace(',', '*')
statement = statement.replace('.', ',')
statement = statement.replace('*', '.')

print(statement)