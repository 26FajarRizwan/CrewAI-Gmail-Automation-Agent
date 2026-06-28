#Block of statements that perform a specific task.
#generally, a function is a block of code that only runs when it is called.

#general syntax
#def function_name(parameter1, parameter2, ...):
    #some work
    #func_name(parameter1, parameter2, ...)#function call

print("function for sum")
def sum(a,b):
    s=a+b
    return s  # Returns the sum of a and b

sum(2,20)  # Function call with arguments 2 and 20
print("the sum is", sum(2,20))  # Prints the result of the function call    

def sub(a,b):
    s=a-b
    return s  # Returns the difference of a and b

print("the sub is", sub(20,2))  # Prints the result of the subtraction

def mul(a,b):
    s=a*b
    return s  # Returns the product of a and b

print("the mul is", mul(2,20))  # Prints the result of the multiplication

def div(a,b):
    if b == 0:
        return "Division by zero is not allowed"  # Handle division by zero
    s = a / b
    return s  # Returns the quotient of a and b

print("the div is", div(20,2))  # Prints the result of the division

print("Function to calculate the average of three numbers")
def average(a, b, c):
    s = (a + b + c) / 3
    return s  # Returns the average of a, b, and c

print("the average is", average(10, 20, 30))  # Prints the result of the average calculation

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"  # Handle negative input
    elif n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i  # Calculate factorial iteratively
        return result  # Returns the factorial of n

print("the factorial is : ", factorial(2))  # Prints the result of the factorial calculation

# Type of functions
# 1. Built-in functions: These are pre-defined functions in Python, such as print(), len(), etc.
# 2. User-defined functions: These are functions defined by the user to perform specific tasks.
# 3. Lambda functions: These are small anonymous functions defined using the lambda keyword.
# 4. Recursive functions: These are functions that call themselves to solve a problem.
# 5. Higher-order functions: These are functions that take other functions as arguments or return them as results.
# 6. Generator functions: These are functions that use the yield statement to return an iterator.
# 7. Asynchronous functions: These are functions defined with the async keyword, allowing for asynchronous programming.
# 8. Decorator functions: These are functions that modify the behavior of other functions.
# 9. Context manager functions: These are functions that manage resources using the with statement.
# 10. Static methods: These are methods defined within a class that do not require an instance of the class to be called.
# 11. Class methods: These are methods that operate on the class itself rather than instances
# 12. Instance methods: These are methods that operate on instances of a class.
# 13. Abstract methods: These are methods defined in an abstract class that must be implemented by subclasses.
# 14. Synchronous functions: These are functions that execute sequentially, blocking the program  until they complete.
# 15. Non-blocking functions: These are functions that allow the program to continue executing while waiting for a task to complete, often used in asynchronous programming.
# 16. Callback functions: These are functions passed as arguments to other functions, to be executed later.
# 17. Event handler functions: These are functions that respond to events, such as user interactions or system events.
# 18. Signal handler functions: These are functions that handle signals sent by the operating system      
# 19. Coroutine functions: These are functions that can pause and resume execution, allowing for cooperative multitasking.
# 20. Method functions: These are functions defined within a class that operate on instances of
# the class, typically using the self parameter to access instance attributes and methods.
# 21. Property functions: These are functions that define properties in a class, allowing for controlled access to instance attributes.
# 22. Class functions: These are functions that operate on the class itself, typically using    the cls parameter to access class attributes and methods.
# 23. Static functions: These are functions that do not require an instance of the class to be called, and are defined using the @staticmethod decorator.
# 24. Instance functions: These are functions that operate on instances of a class, typically

print("apna college",end=" ")
print("python functions", end=" ")  # Example of using end parameter in print function
print("hello world")  # Prints "hello world" to the console
print("hello world", "python functions")  # Prints multiple strings with a space in between

#default parameters
def greet(name="Guest"):
    print("Hello,", name)  # Prints a greeting message with the provided name or "Guest" if no name is given
greet()  # Calls the function with default parameter
greet("Alice")  # Calls the function with a specific name

print("PRACTICE QUESTIONS")
print("1.WAF to print the length of a list. ( list is the parameter)")

cities=["lahore","karachi","islamabad","murree"]

heroes=["ironman","superman","batman","thor"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

print("2. WAF to print the elements of a list in a single line. ( list is the parameter)")
def print_list(list):
    for items in list:
        print(items, end=" ")

print_list(heroes)

print("3. WAF to find the factorial of n. (n is the parameter)")
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"  # Handle negative input
    elif n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i  # Calculate factorial iteratively
        return result  # Returns the factorial of n

print("the factorial is : ", factorial(20)) 


print("4.  WAF to convert USD to INR.")
def converter(usdvalue):
    inrvalue = usdvalue * 83
    print(usdvalue, "USD=", inrvalue, "inr")

converter(1837)

print("4. WAF to print odd if the number taken from user is odd or else even ")
def check(n):
    if (n%2 == 0): 
        return "even"
    elif (n%2 !=0):
        return "odd"

n= int(input("enter the number: "))
print("The number is: " , check(n))


