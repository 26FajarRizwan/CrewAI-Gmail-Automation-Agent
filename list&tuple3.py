# #List and tuples in Python
# # Lists and tuples are both used to store collections of items in Python,
# #  but they have some key differences.
# # Lists are mutable, meaning they can be changed after creation,
# # while tuples are immutable, meaning they cannot be changed.
# # Lists are defined using square brackets, while tuples are defined using parentheses.
# marks=[90, 80, 70.8, 60.5, 50]
# print(marks)  # Output: [90, 80, 70.8, 60.5, 50]
# print(type(marks))  # Output: <class 'list'>
# print(len(marks))  # Output: 5
# print(marks[0])  # Output: 90
# print(marks[1:3])  # Output: [80, 70.8]

# #lists can also store data of diff datatypes
# #list slicing
# marks=[90, 80, 70.8, 60.5, 50]
# print(marks[1:4])  # Output: [80, 70.8, 60.5]
# #also contains negative index
# print(marks[-1])  # Output: 50
# print(marks[-3:-1])  # Output: [70.8, 60.5]

#list method
list=[1, 2, 3, 4, 5]
list.append(6)  # Adds 6 to the end of the list
print(list)  # Output: [1, 2, 3, 4, 5, 6]

#sorting a list arrange the values in order asend or descend
list2=[3,5,68,3,5.6,7.8,54]
list2.append(6)  # Adds 6 to the end of the list
list2.sort()  # Sorts the list in ascending order
print(list2)  # Output: [3, 3, 5, 5 6, 7.8, 54, 68]

list=[1, 2, 3, 4, 5]
print(list.sort(reverse=True))  # Sorts the list in descending order
print(list)  # Output: [5, 4, 3, 2, 1]

#can also sort strings according to their ascii values
list3=['a', 'b', 'c', 'd', 'e'] 
list3.sort()  # Sorts the list in ascending order
print(list3)  # Output: ['a', 'b', 'c', 'd', 'e']
list3.sort(reverse=True)  # Sorts the list in descending order
print(list3)  # Output: ['e', 'd', 'c', 'b  ', 'a']

list4=['a', 'b', 'c', 'd', 'e']
list4.reverse()  # Reverses the order of the list   
print(list4)  # Output: ['e', 'd', 'c', 'b', 'a']

 #list index insert
list5 = [1, 2, 3, 4, 5]
list.insert(2, 10)  # Inserts 10 at index 2
print(list5)  # Output: [1, 2, 10, 3, 4, 5]

#remove method
list6 = [1, 2, 3, 4, 5]
list6.remove(3)  # Removes the first occurrence of 3 from the list      
print(list6)  # Output: [1, 2, 4, 5]

#pop method
list7 = [1, 2, 3, 4, 5]
list7.pop()  # Removes the last element from the list
print(list7)  # Output: [1, 2, 3, 4]

# Tuple example
# Tuples are similar to lists, but they are immutable.

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)  # Output: (1, 2, 3, 4, 5)
print(type(tuple1))  # Output: <class 'tuple'>

tuple2 = (1, 2, 3, 4, 5)
print(tuple2[0])  # Output: 1
print(tuple2[1:3])  # Output: (2, 3)

# Tuples can also store data of different data types
tuple3 = (1, "Hello", 3.14, True)
print(tuple3)  # Output: (1, 'Hello', 3.14, True)

tup=()
print(tup)
print(type(tup))

#tuple slicing
tup=[1,2,3,4,5,6,7,8,9,10]
print(tup[1:5])  # Output: [2, 3, 4, 5]
print(tup[-1])  # Output: 10

#tuple index
print(tup.index(5))  # Output: 4 (index of the first occurrence of 5)
print(tup.index(10))  # Output: 9 (index of the first occurrence
