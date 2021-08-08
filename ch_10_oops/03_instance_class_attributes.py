class Employee:
    company= 'Google'
    # salary= 900
    
vid= Employee()
ron= Employee()
shyam= Employee()
# vid.salary= 300
# ron.salary= 500
Employee.salary= 900
print(vid.salary)
print(ron.salary)
print(shyam.salary)
shyam.salary=100000
print(shyam.salary)
print(vid.company)
print(ron.company)
Employee.company= 'Youtube'
print(vid.company)
print(ron.company)