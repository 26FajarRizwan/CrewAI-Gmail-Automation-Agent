movies=[]
mov1=input("Enter 1st movie name: ")
mov2=input("Enter 2nd movie name: ")
mov3=input("Enter 3rd movie name: ")    

movies.append(mov1)
movies.append(mov2)     
movies.append(mov3)
print("Movies list:", movies)   
movies.sort()  # Sorts the list in ascending order
print("Sorted Movies list:", movies)  # Output: Sorted list of movies

#palindrome check 
#def of palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

#question to check list is palindrome or not

list1= [1, 2, 3, 2, 1]
list2= [1, 2, 3, 4, 5]

copy_list1 = list1.copy()
copy_list1.reverse()  # Reverses the list

if(copy_list1==list1):
    print("List1 is a palindrome")
else:
    print("List1 is not a palindrome")
    
list3=["m", "a", "d", "a", "m"]
copy_list3 = list3.copy()
copy_list3.reverse()  # Reverses the list
if(copy_list3==list3):
    print("List3 is a palindrome")
else:
    print("List3 is not a palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()  # Reverses the list   
if(copy_list2==list2):
    print("List2 is a palindrome")
else:
    print("List2 is not a palindrome")

#count the number of students with the A grade in tuple

grades = ("A", "B", "C", "A", "A", "B", "C", "A")
print(grades.count("A"))  # Output: 4

# store the values in list and then sort the list
grade=("A","F","C","G","R")
grade.sort()
print(grade)
