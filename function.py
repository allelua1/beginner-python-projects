def my_function():
    print("Hello from a function")
my_function()

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32)*5/9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(50))

def add( a, b ):
    return a + b
sum = add(2,3)
print(sum)
# positional arguments
def my_name(fname, lname, age=23):
    print(fname + " " + lname + " I am " + str(age) + " years old")
my_name("Ally", "Muna")
# positiona & keyword arguments
def my_details(name, major, year, university):
    print("My Name is ", name , ". I am majoring in ", major , ". This is my ", year , " year at ", university )
my_details("Allelua", major = "APT", year = "third", university = "USIU-AFRICA")

def function_list(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits = ["Apple", "Banana", "mango"]
function_list(my_fruits)

def function_dict(person):
    print("Name: ", person["name"])
    print("Age: ", person["age"])
my_person = {"name":"Ally", "age": 22}
function_dict(my_person)
# *argument: when you do not know the number of argument you can pass in ur function
def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_function(1,2,4))
print(my_function(20,50))

def my_function(*args):
    print("First argument: ", args[0])
    print("Second argument: ", args[1])
    print(" All arguments: ", args)
my_function("Abhi", "Ayla","Beltrand")


# parameters & argument
def greeting(name):
    print("Hello", name)
greeting("Benigne")

# maximun number using *args
def maximunNumber(*numbers):
    if len((numbers)) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print("Maximun number is: ", maximunNumber(50,20,40,100,150))

# **kwargs
def my_function(**myvar):
    print("Name: ", myvar["name"])
    print("Age: ", myvar["age"])
    print("All data: ", myvar)

my_function(name= "Muna", age = 23, city="Nairobi")

def my_function(username, **detail):
    print("Username: ", username)
    print("Additional details: ")
    for key, valu in detail.items():
        print(" ", key, " : ", valu)
my_function("Muna123", age = 23, city = "nairobi", hobby = "Coding")
