# # # # # # # # # course = "python \"progtamming "
# # # # # # # # # print(course)
# # # # # # # # # \""
# # # # # # # # # \'
# # # # # # # # # \\
# # # # # # # # # \n new line
# # # # # # # # course = "       python programming      "
# # # # # # # # print(course.upper())
# # # # # # # # print(course.title())
# # # # # # # # print(course.strip())  # for remove spaces
# # # # # # # # print(course.find("pro"))  # print index
# # # # # # # # print(course.replace("p", "j"))
# # # # # # # # print("pro" in course)  # boolean expression result

# # # # # # # # Numbers
# # # # # # # import math
# # # # # # # print(10 + 3)
# # # # # # # print(10-3)
# # # # # # # print(10*3)
# # # # # # # print(10/3)
# # # # # # # print(10//3)
# # # # # # # print(10 % 3)
# # # # # # # print(10**3)  # exponent power

# # # # # # # print(round(2.9))
# # # # # # # print(abs(-2.9))
# # # # # # # print(math.ceil(2.2))
# # # # # # # print(round(2.5))
# # # # # # # print(round(2.2))
# # # # # # # print(math.factorial(23))
# # # # # # # print(math.fabs(32.32))
# # # # # # # print(math.sqrt(25))

# # # # # # # falsy value
# # # # # # # ""
# # # # # # # 0
# # # # # # # none

# # # # # # # Fundamentals of computer programming
# # # # # # # comparision operator
# # # # # # a = ("bag" == "BAG")
# # # # # # print(a)

# # # # # # temperature = 10
# # # # # # if temperature >= 30:
# # # # # #     print("its warm")
# # # # # # elif (temperature >= 20 and temperature < 29):
# # # # # #     print("its good")
# # # # # # else:
# # # # # #     print("its cold")
# # # # # # print("done")  # always executed


# # # # # # # ternary operator
# # # # # # age = 22
# # # # # # if age >= 18:
# # # # # #     message = "eligible"
# # # # # # else:
# # # # # #     message = "not eligible"

# # # # # # print(message)

# # # # # # highincome = False
# # # # # # goodcredit = True

# # # # # # if highincome and goodcredit:
# # # # # #     print("eligible")
# # # # # # else:
# # # # # #     print("try again")
# # # # # # print("yayyayayayayayayay")

# # # # # # age = 22
# # # # # # if 18 <= age < 65:
# # # # # #     print("eligible")

# # # # # # #loops

# # # # # # for number in range(10):
# # # # # #     print("heloo", number + 1, (number + 1) * ".")

# # # # # # for number in range(0, 50, 3):
# # # # # #     print("muskurahat", (number+1)*"😙")

# # # # # # for number in range(0, 10, 2):
# # # # # #     word = "helo"
# # # # # #     print(word, number+1, (number+1)*"🙂")

# # # # # # for else
# # # # # successful = False
# # # # # for number in range(3):
# # # # #     print("attemt")
# # # # #     if successful:
# # # # #         print("successful")
# # # # #         break

# # # # # else:
# # # # #     print("Attempted 3 times and failed")

# # # # # for x in range(5):
# # # # #     for y in range(3):
# # # # #         print(f"({x},{y})")

# # # # # # iterables
# # # # print(type(range(5)))

# # # for x in "Python":
# # #     print(x)

# # # for num in [1, 2, 3, 4, 5]:
# # #     print(num)

# # # for item in "shopping_cart":
# # #     print(item)

# # # #while loop

# # # number = 100
# # # while number > 0:
# # #     print(number)
# # #     number = number//2

# # # command = ""
# # # while command != "quit":
# # #     command = input(">")
# # #     print("ECHO", command)

# # # practice question
# # count = 0
# # for number in range(1, 10):
# #     if (number % 2 == 0):
# #         count += 1
# #         print(number)
# # print(f"we have {count} even numbers")

# # functions
# def greet(fn, ln):
#     print(f"Hi {fn} and {ln}")
#     print("Welcome abroad")
#     print("Enjoy your journey")


# greet("Fajar", "Ayesha")

# # functions that perform a task
# # functions that return a value

def greet(name):
    return f"hi {name}"


print(greet("Ayesha"))


def increment(num, by):
    return num+by


print(increment(2, 20))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
