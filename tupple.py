"""mytupple = (1, 2, 3, 4, 5)
print("Original tuple:", mytupple)
print("Length of the tuple:", len(mytupple))

mylist = list(mytupple)
mylist.append(6)
mytupple = tuple(mylist)
print("Modified tuple:", mytupple)"""

# SET
"""myset = {1, 2, 3, 4, 5}
print("Original set:", myset)
print("Length of the set:", len(myset))"""

# Dictionary
mydict = {
    "name": "John",
    "age" : 30,
    "city": "New York"

}
print("Original dictionary:", mydict)
x = mydict["name"]
print(x)
age = mydict.get("age")
print(age)
mydict = dict(name = "Allelua", age = 23, country = "Kenya")
print(mydict)
print(mydict.keys())
mydict["major"] = "APT"
print(mydict)

print(mydict.values())
for data, values in mydict.items():
    print(data, "\t", values)

# updating
mydict.update({"University":"USIU-AFRICA"})
print(mydict)
# deleting or removing

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

del mydict["major"]
print(mydict)

mydict.clear()
print(mydict)

# Nested dictionary
studentrecord = {
    "Student1":{
        "name": "Benigne",
        "age": 24,
        "major":"APT"
    },
    "Student2":{
        "name": "Muna",
        "age" : 23,
        "Major": "APT"
    },
    "Student3":{
        "name": "Diane",
        "age" : 24,
        "Major": "Pharmacy"
    },
    "Student4":{
        "name": "Racheal",
        "age" : 22,
        "Major": "Data Science"
    }
    
}
print(studentrecord)
print(studentrecord.keys())
print(studentrecord.values())

print(studentrecord["Student4"]["name"])

for student, record in studentrecord.items():
    print(student)
    for records in record:
        print(records, ":", record[records])
