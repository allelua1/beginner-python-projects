num1 = 11
print(num1)
# strings
name = "Allelua"
print(name)
a, b = 5, 10
print(a, b)
#Lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
print(mylist)

total = 0
for x in mylist:
    print(x)
    total += x
print("Total:", total)
fruits=["apple", "banana", "cherry"]
x,y,z = fruits
print(x)

print(y)
print(z)

# multiplication table
while True:
   number = input("Enter a numbeer to generate its multiplication table: ")

   if number.lower() =="quit":
       print("Exiting the program. Goodbye!")
       break
   try:
       number =int(number)
   except ValueError:
        print("Please enter a valid number or 'quit'.")
        continue
   print(f"Multiplication Table for {number}:")
   for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")