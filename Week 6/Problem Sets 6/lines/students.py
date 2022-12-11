students = [] 

with open('students.csv') as file:
    for line in file:
        name, house = name.rstrip().split(',')
        students.append(f"{name} is in {house}")

for students in sorted(students):
    print(student)