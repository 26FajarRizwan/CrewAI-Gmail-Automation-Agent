#Range function
#returns a sequence of numbers,starting from 0 by default, and increments by 1 (by default), and stops before a specified number.   
#The range() function is commonly used in for loops to iterate over a sequence of numbers.
#It can also be used to generate a list of numbers.
#Syntax: range(start, stop, step)

#start: The value of the first number in the sequence (default is 0).
#stop: The value at which the sequence stops (exclusive).
#step: The difference between each number in the sequence (default is 1).

seq=range(10)  # Generates numbers from 0 to 9
for i in seq:
    print(i)  # Prints numbers from 0 to 9
print(seq)  # Output: range(0, 10)


print("Another method to print the range")
for i in seq:
    print(i)  # Prints numbers from 0 to 9

print("range stop")
for i in range(10):
    print(i) 

print("range start and stop")
for i in range(5, 15):  # Generates numbers from 5 to 14
    print(i)  # Prints numbers from 5 to 14

print("range start, stop, and step")
for i in range(2, 20, 3):  # Generates numbers from 2 to 19 with a step of 3
    print(i)  # Prints numbers: 2, 5, 8, 11, 14, 17     

print("Practice questions")

print("1. Print numbers from 0 to 100 using range function")
for i in range(101):
    print(i)

print("2.print numbers from 100 to 1 using range function")
for i in range(100,0,-1):
    print(i)    

print("3.print the multiplication table of a number using range function ")
n = int(input("Enter a number for multiplication table: "))
for i in range(1,11):  # Generates numbers from 1 to 10
    print(n * i)  # Prints the multiplication table of n    

print("#PASS STATEMENT IN RANGE FUNCTION")
print("pass is a null statement that does nothing. It is used as a place holder for future code.")

for i in range(5):
    pass  # This loop does nothing, but it is syntactically correct
print("This is after the pass statement in the loop.")

print("Practice questions")

print("1. Find the sum of first n numbers using range function")
n = int(input("Enter a number: "))
sum=0
for i in range(n+1):
    sum += i  # Adds each number to the sum
print("The sum of first", n, "numbers is:", sum)

print("__________________________________________")
print("2. using while loop")
n=int(input("enter the number:  "))
sum=0
i=0
while i<=n:
    sum += i  # Adds each number to the sum
    i += 1
print("The sum of first", n, "numbers is:", sum)

print("______________________________________________")
print("3. Find the factorial of first n numbers using range function")
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i  # Multiplies each number to get the factorial
print("The factorial of", n, "is:", factorial)





