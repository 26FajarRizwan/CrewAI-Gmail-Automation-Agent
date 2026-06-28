str1="This is a string.\nIt contains a newline character."
print(str1)
#concatenation
str2 = "Hello, " + "world!" 
print(str2)
#length of string
str3 = "Hello, world!"
print(len(str3))

#string functions
#ends with
str4 = "Hello, world!"
print(str4.endswith("world!"))  # Output: True
print(str4.endswith("Hello"))  # Output: False

#For Capatilization
str5 = "hello, world!"
print(str5.capitalize())  # Output: Hello, world!

#for replacing
str6 = "Im studying Python from apna college."
print(str6.replace("o", "a"))  # Output: Im studying Python fram apna callege.

#For Find Functions
str7="Im familiar with Python."
print(str7.find("familiar"))  # Output: 3
print(str7.find("Java"))      # Output: -1 (not found)

#for count functions
str8 = "banana"
print(str8.count("a"))  # Output: 3

