# lambda arguments : expression
sum = lambda a, b: a + b
print(sum(1,2))

# lambda with map()
numbers = [1,2,3,4,5]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)

# recursion

def countdown(n):
    if n <= 0:
        print("DONE!")
    else:
        print(n)
        countdown(n-1)
countdown(5)

# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print("Factorial: ", factorial(5))

# fibonacci
def fibonacci(n):
    if n <= 1 :
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonnacci: ", fibonacci(7))