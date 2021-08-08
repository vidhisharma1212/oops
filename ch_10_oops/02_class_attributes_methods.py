class Employee:
    company= 'Google'
    salary= 900
    
vid= Employee()
ron= Employee()
vid.salary= 300
ron.salary= 500

print(vid.salary)
print(ron.salary)
print(vid.company)
print(ron.company)
Employee.company= 'Youtube'
print(vid.company)
print(ron.company)