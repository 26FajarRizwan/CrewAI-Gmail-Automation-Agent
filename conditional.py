# age=input("Enter your age:  ")
# if (age>="18"):
#     print("You are eligible to vote. And u r also eligible for driving liscence.")
# elif (age>="16"):
#     print("You are not eligible to vote. And u r also not eligible for driving liscence.")
# else:
#     print("Sorry go back to home")

#2nd example

# marks=int(input("Enter your marks: "))
# if (marks>=90):
#     print("You got A+ grade.")
# elif (marks>=80 and marks<90):
#     print("You got A grade.")
# elif (marks>=70 and marks<80):
#     print("You got B grade.")
# elif (marks>=60 and marks<70):
#     print("You got C grade.")
# elif (marks>=50 and marks<60):
#     print("You got D grade.")
# else:
#     print("You got F grade. Better luck next time.")

#nesting if-else example
age = int(input("Enter your age: "))
if (age >= 18):
    print("You are eligible to vote.")
    if age >= 21:
        print("You are also eligible for driving license.")
    else:
        print("You are not eligible for driving license yet.")
else:
    print("You are not eligible to vote or drive yet.")
