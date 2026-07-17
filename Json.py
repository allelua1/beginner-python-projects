import json
student ='{"name":"John", "age":20, "City":"New York"}'
"""Convert JSON to python"""
s1 = json.loads(student)
print(s1["name"])

"""Converting python into JSON"""
x = {
    "Name": "John",
    "Age": 23,
    "city":"New York"
}
y = json.dumps(x)
print(y)

print(sum([3,4,5]))