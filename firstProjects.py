# in order to get a community service certificate, you need to work 100 hours.
#  3 days a week and 3 hours per week. you have to register for  the  community service

""" name = input("Enter Your Name:")
sid = input("Enter Your Student ID:")
major = input("Enter Your major:")
print(name + "  " + sid + "  " + major)
have_you_registered = input("Have you registered for the community service? (yes/no): ")

if have_you_registered.lower() == "yes":
    print("Great! You can start working on your community service hours.")
    print("You need to work a total of 100 hours.")
    print("That's 3 hours per week for 33 weeks.")
    certificate = input("Do you want to get a community service certificate? (yes/no):")
    if certificate.lower() == "yes":
        print("You will receive a community service certificate after completing 100 hours.")
    else:
        print("You can still work on your community service 90 hours, but you won't receive a certificate.")
else:
    print("Please register for the community service to start working on your hours.") """

# 1. number guessing game
""" guess  = int(input("Enter a guessed number bewteen 1 and 100:"))
counter = 0
while  guess >1 or guess <100:
    number = int(input("Invalid input. Please enter a number you are guessing between 1 and 100:"))
    counter += 1
    if number >  guess:
       print("Too high! Try again.")
    elif number < guess:
         print("Too low! Try again.")
    elif number == guess:
        print("Congratulations! You guessed the correct number.")
        break

print("You took", counter, "attempts to guess the number.")
 """
# 2. simple calculator
""" a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
operators = ["+", "-", "*", "/"]
for operator in operators:
    if operator == "+":
        print( a, " + ", b, " = ", a + b)
    elif operator == "-":
        print( a, " - ", b, " = ", a - b)
    elif operator == "*":
        print( a, " * ", b, " = ", a * b)
    elif operator == "/":
        if b != 0:
            print( a, " / ", b, " = ", a / b)
        else:
            print("Error: Division by zero is not allowed.") """

""" user_type = ""
while user_type != "quit":
        user_type = input("Enter 'quit' to exit or any key to continue: ")
        if user_type == "quit":
                print("Exiting the program.")
                break
        else:
                print("Continuing the program.")
                a = int(input("Enter First Number: "))
                b = int(input("Enter Second Number: "))
                operator = input("Enter an operator (+, -, *, /): ")
                if operator == "+":
                    print(a, " + ", b, " = ", a + b)
                elif operator == "-":
                    print(a, " - ", b, " = ", a - b)
                elif operator == "*":
                    print(a, " * ", b, " = ", a * b)    
                elif operator == "/":
                    if b != 0:
                        print(a, " / ", b, " = ", a / b)
                    else:
                        print("Error: Division by zero is not allowed.") """

# 3. UNIT CONVERTER
choice = ""
""" while choice != "quit":
    choice = input("Enter 'C' to convert Celsius to Fahrenheit, 'F' to convert Fahrenheit to Celsius, or 'quit' to exit: ").strip().lower()

    if choice == "quit":
        print("Exiting the program.")
        break
    elif choice == "c":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == "f":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid choice. Please enter 'C', 'F', or 'quit'.") """

# 4. BASIC ATM SIMULATOR
""" fixed_balance = 1000
print("Welcome to the ATM Simulator!")
print(f"Your current balance is: ${fixed_balance:.2f}")

while True:
    print("\nPlease choose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4):").strip()

    if choice == "1":
        print(f"Your current balance is : ${fixed_balance:.2f}")
    elif choice == "2":
        try:
            deposit_amount = float(input("Enter the amount to deposit:").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if deposit_amount > 0:
            fixed_balance += deposit_amount
            print(f"Successfully deposited ${deposit_amount:.2f}")
            print(f"Your new balance is : ${fixed_balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    elif choice == "3":
        try:
            withdraw_amount = float(input("Enter the amount to withdraw:").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if withdraw_amount > 0:
            if withdraw_amount <= fixed_balance:
                fixed_balance -= withdraw_amount
                print(f"Successfully withdrew ${withdraw_amount:.2f}")
                print(f"Your new balance is : ${fixed_balance:.2f}")
            else:
                print("Insufficient funds. Please enter a smaller amount.")
        else:
            print("Withdrawal amount must be positive.")
    elif choice == "4":
        print("Thank you for using the ATM Simulator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
             """

# 5. MULTIPLICATION TABLE Generator
"""
while True:
    number = input("Enter a number to generate its multiplication table (or type 'quit' to exit): ").strip()

    if number.lower() == "quit":
        print("Exiting the program. Goodbye!")
        break

    try:
        number = int(number)
    except ValueError:
        print("Please enter a valid number or 'quit'.")
        continue

    print(f"Multiplication Table for {number}:")

    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")"""
# Simple login system
"""fixed_username = "admin"
fixed_password = "12345"

attempt = 0
while attempt < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == fixed_username and password == fixed_password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password.")
        
        print(f"You have {2 - attempt} attempts left.")
    attempt += 1"""
# Even / Odd Number Checker

"""while True:
    number = input("Enter a number to check if it's even or odd (or type 'quit' to exit): ").strip()

    if number.lower() == "quit":
        print("Exiting the program. Goodbye!")
        break

    try:
        number = int(number)
    except ValueError:
        print("Please enter a valid number or 'quit'.")
        continue

    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")"""

# 8. Pattern Printing
for i in range(1, 6):
    print("*" * i)
    # rectangle pattern
for i in range(1,6):
    for j in range(1,6):
        print("@", end=" ")
    print("")
for i in range(1,6):
    print("* "* (6-i))

for i in range(1,6):
    for j in range(1, i+1):
        print("*", end=" ")
    print("")
    
for i in range(6,1,-1):
    for j in range(1,i):
        print("*", end=" ")
    print("")
    
for i in range(1,6):
    for k in range(1,i+1):
        for j in range(1,5):
            print("")
        print("&", end=" ")
    print("")


# 9. Fibonacci Sequence Generator
"""n = int(input("Enter the number of terms for the Fibonacci sequence: "))
a, b = 0,1
while a < n:
    print(a, end=" ")
    a, b = b, a + b"""

# Simple Quiz Game
questions = [
    {
        "question": "Where do you come from?",
        "answer": "Rwanda"
    },
    {
        "question": "How old are you?",
        "answer": "23"
    },
    {
        "question": "What's your name?",
        "answer": "Allelua"
    },
    {
        "question": "What's your ID?",
        "answer": "670449"
    }
]

counter = 0

for item in questions:
    user_answer = input(item["question"] + " ").strip()
    if user_answer.lower() == str(item["answer"]).lower():
        print("Correct!")
        counter += 1
    else:
        print("Wrong! The correct answer is:", item["answer"])

print("Your score is:", counter)

    


