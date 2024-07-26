emp_id = 101                # int data type
emp_name = 'Usama Omar'     # string data type
emp_salary = 7000.90        # float data type
emp_job = 'Web Developer'   # string data type
emp_city = 'Cairo'

# Usama Omar works as Web Developer and lives in Cairo
print(emp_name + ' works as ' + emp_job + ' and lives in ' + emp_city)

print('-------------- Casting --- Convert from data type to another -------from int, float to string ----')
# ex :  Usama Omar takes salary = 7000.55
print(emp_name + ' takes salary = ' + str(emp_salary) )

# ex: Usama Omar has code = 101
print(emp_name + ' has code = ' + str(emp_id) )

print('---- casting ----- convert from float to int --------------------')
print(emp_salary) # 7000.55
print( int(emp_salary)  )  # 7000
