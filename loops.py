#loops are used to repeat a block of code multiple times

#while loop
count=1
while count <= 5:
    print("Helo")
    count+= 1

print(count)  # This will print the final value of count after the loop ends.

i=1
while i <= 100:
    print("hy",i)
    i += 1
print("Loop ended")

i=5
while i>=1:
    print(i)
    i-=1
print("Loop ended")

#qs 1
i=1
while i <=100:
    print(i)
    i+=1
print("printed from 1 to 100")

#qs 2
i= 100
while i>=1:
    print(i)
    i-=1
print("printed from 100 to 1")

#qs 3
#multiplication table of n number
n = int(input("Enter a number for multiplication table: "))
i = 1
while i <= 10: 
    print(n*i)
    i += 1
print("Multiplication table of", n, "completed.")

#qs 4
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(nums):
    print(nums[idx])
    idx += 1

#qs 5
print("searching for the number x in the tuple using loop")

af=(1,4,9,16,25,36,49,64,81,100)
print(af)
x=int(input("enter the value u want to find:"))
i=0
while i < len(af):
    if af[i] == x:
        print("Found x at index", i)
        break
    i += 1
else:
    print("x not found in the tuple")

#BREAK AND CONTINUE STATEMENT

i=1
while i <= 10:
    print(i)
    if (i==5):
        print("Breaking the loop at 5")
        break
    i +=1

i=0
while i<=5:
    if(i==3):
        i+=1
        continue  # Skip the rest of the loop when i is 3
    print(i)
    i += 1

print("for printing odd numbers from 1 to 10")
i=0
while i<=10:
    if(i%2 ==0):
        i+=1
        continue  # Skip even numbers
    print(i)
    i += 1

print("for printing even numbers from 1 to 10  ")
i=0
while i<=10:
    if(i%2 !=0):
        i+=1
        continue  # Skip odd numbers
    print(i)
    i += 1

