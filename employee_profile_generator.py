# Employee Profile Generator 
first_name = 'John' # Employee's first name
last_name = 'Doe' # Employee's last name
full_name = first_name + ' ' + last_name # Employee's first name + last name = full name
address = '123 Main Street' # Employee's street name
address += ', Apartment 4B' # Employee's building 
employee_age = 30 # Employee's age
employee_info = full_name + ' is ' + str(employee_age) + ' years old' # Employee's full name + age = employee's info
print(employee_info) # output: full name + is + age + years old
experience_years = 5 # Employee's years of experience
experience_info = 'Experience: ' + str(experience_years) + ' years' # Employee's years of experience = employee's experience info
print(experience_info) # output: Experience + experience years + years 
position = 'Data Analyst' # Employee's position in company 
salary = 75000 # Employee's yearly salary 
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}' # F-string: employee's full name, age, position, salary &
print(employee_card) # output: Employee + full name + Age + employee age + Position + position + Salary + salary = employee card
employee_code = 'DEV-2026-JD-001' # Employee company code
department = employee_code[0:3] # Slicing the string DEV-2026-JD-001 to get department 
print(department) # output: sliced string = department 
year_code = employee_code[4:8] # Slicing the string DEV-2026-JD-001 to get year 
print(year_code) # output: sliced string = year
initials = employee_code[9:11] # Slicing the string DEV-2026-JD-001 to get initials
print(initials) # output: sliced string = initials
last_three = employee_code[-3:] # Slicing the string DEV-2026-JD-001 to get last three digits 
print(last_three) # output: sliced string = last three digits