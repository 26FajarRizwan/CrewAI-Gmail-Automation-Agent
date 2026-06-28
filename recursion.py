#recursion 
#when a function calls itself repeatedly
#loops and recursion are inter related

print("RECURSIVE FUNCTION")
def show(n):
    if (n==-1): #base case is important otherwise it will become a loop and dont run
        return
    print(n)
    show(n-1)
    print("end")

show(5) #5, 4=n-1, 3=n-2, 1

#call stack
#block of functions 
#factorial
def fact(n):
    if (n==0 or n==1):  #base case
        return 1
    else:
        return n * (fact(n-1))
    
print(fact(4))
print(fact(3))
print(fact(7))

print("Practice questions")
print("1. WA recursive function to print the sum of first n natural numbers")
def sum(n):
    if(n==0):
        return 0
    return sum(n-1) + n

print(sum(8))
    
print("2. WARF to print all elements in a list")
def print_list(list, idx=0):
    if(idx== len(list)): 
        return
    print(list[idx])
    print_list(list, idx+1)

cars=["BMW","Audi","Mercedes","Ferrari","Toyota hillux","mehran"]

print_list(cars)