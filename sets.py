#sets in python
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets, and do not allow duplicate values.
#sets are mutable but its elements are immutable

# Create a set
#nums={1, 2, 3, 4, 5}
#set2={1,2,2,2,2} repeated elements store only once item at one time

#null_set=set()  # Creating an empty set
# print(null_set)  # Output: set()

collection = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(collection)

set1={1,2,3,4,2,3,5,"hello",2,"world"}
print(set1)
print(len(set1))

emptyset=set()
print(emptyset)
print(type(emptyset))

#SET METHODS
#to add
emptyset.add(3)
print(emptyset)

#remove
emptyset.remove(3)
print(emptyset)

#clear method
print(len(collection))
collection.clear()
print(len(collection))

#pop method
set2={"hello","World","apnacollege","coding",3,"Python",947}
print(set2.pop())
print(set2.pop())

#union
set4={1,2,3,4,5}
set5={3,5,6,8}
print(set4.union(set5))  # Output: {1, 2, 3, 4, 5, 6, 8}

#intersection
set6={1,2,6,9}
set7={2,6,7,8,0}
print(set6.intersection(set7))  # Output: {2, 6}

