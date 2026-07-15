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
# list comprehension
squares = [x**2 for x in numbers if x % 2 == 0]
print(squares)

newlist =[ x for x in mylist if "a" in x]
print(newlist)

numbers.sort(reverse=True)
print(numbers)