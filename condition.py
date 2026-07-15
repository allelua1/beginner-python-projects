"""x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More") -4"""
# For Loop
"""word =["cat", "window", "defenestrate"]
for w in word:
    print(w, ":", len(w))"""
# boolean
"""print(bool("Hello"))
print(bool([1, 2, 3]))
x= 110
print(isinstance(x, int))

def myfunction():
    return True
if myfunction():
    print("YES!")
else:
    print("NO!")"""

# Challenge: Booleans 
"""print(10 > 9)
print(10 == 9)
print(bool("Hello"))
print(bool(0))
"""
# Ternary Operator
"""day = input("Enter the day of the week: ").strip().lower()
x = "WEEKEND" if day in {"saturday", "sunday"} else "WEEKDAY" if day in {"monday", "tuesday", "wednesday", "thursday", "friday"} else "INVALID DAY"
print(x)
"""
# Membership Operators
# fruits = ["apple", "banana", "cherry"]
# if "banana" in fruits:
#     print("Yes, 'banana' is in the fruits list")

# python lists
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist))

numbers = [1, 2, 3, 4, 5]
print(numbers)

numbers.append(6)
print(numbers)

print(numbers[0])

numbers.insert(2, 2.5)
print(numbers)

numbers.remove(3)
print(numbers)
for i in range(len(numbers)):
    print(numbers[i])

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

