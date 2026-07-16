def greeting(name):
    print("Hello ", name)
print(max([1,2,30,10]))

students = [
    {"name":"Benigne", "Marks": 90},
    {"name":"Diane", "Marks": 80},
    {"name":"Ben", "Marks": 95}
    ]
students.sort(key = lambda student : student["Marks"])
for student in students:
    print(student["name"],":", student["Marks"])
print(students)