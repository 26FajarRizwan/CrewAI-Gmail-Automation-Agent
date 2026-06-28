#for loops
#loops are used for sequential traversal of elements in a collection
#for transversing a list, tuple, string, or any iterable

nums=[1,2,3,4,5]
for val in nums:
    print(val)

veg=["potato", "tomato", "onion", "cabbage", "carrot"]
for val in veg:
    print(val)

str="fajar Ayesha"
for char in str:
    if (char == "A" or char == "a"):
        break  # Breaks the loop if 'A' or 'a' is found
    print(char)
else:
    print("End")

str="fajar Ayesha"
for char in str:
    if (char == "A" or char == "a"):
        continue # Continues to the next iteration if 'A' or 'a' is found 
    print(char)
else:
    print("End")

print("Practice questions")
print("1. print the elements of folowing list using a loop")
nums=[1,4,9,16,25,36,49,64,81,100]
print(nums)
for val in nums:
    print(val)

print("2. search for a number in a tuple using a loop")
af=(1,4,9,16,25,36,49,64,81,100 )
x= int(input("Enter the value you want to find:    "))
i=0
for el in af:
    if el == x:
        print("Found", x, "in the tuple")
        break
else:
    print(x, "not found in the tuple")
    i += 1

