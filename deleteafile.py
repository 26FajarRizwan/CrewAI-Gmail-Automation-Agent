#deleting a file using OS MODULE
#module like code library written by another programmer 

# import os
# os.remove("sample.txt")

print(" Practice Questions ")
# print("create a new file using with syntax ")
# with open("practice.txt","w") as f:
#     f.write("HI everyone!!!!\n we are learning file i/o \n")
#     f.write("using java. \n i like programming in java")

print("WAF that replaces all the occurances of java with python in above file")
with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java ", "Python")
print(new_data)

with open("practice.txt","w") as f:
      f.write(new_data)

with open("practice.txt", "r") as f:
    data=f.read()
    word="learning"
    if (word in data):
          print("found")
    else:
        print("not found")

print("WAF to print in which of the file does the word learning occur first print -1 if it is not found")
def check_for_line():
    word="learning"
    data = True
    line_no=1
    with open("practice.txt","r") as f:
         while data:
              data = f.readline()
              if(word in data):
                   print(line_no)
                   return
              line_no +=1

    return -1

print(check_for_line())

print("from a file containing numbers separated by commas print the count of even numbers")
with open("practice2.txt" , "r") as f:
    data = f.read()
    print(data)


