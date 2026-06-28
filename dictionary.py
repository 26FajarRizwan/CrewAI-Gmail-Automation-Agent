#Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
# Create a dictionary

mydict={
    "name":"fajar",
    "age": 18,
    "Subjects":["Python","C++","SQL"],
    "Topics":("Dic","list","Tuple"),
    "IS_Student":True,
    "Marks": 90.5,
}

print(mydict)
print(mydict["name"])  # Accessing value by key
print(mydict["age"])   # Accessing value by key 

mydict["name"]="fajar rizwan"  # Updating value by key
print(mydict["name"])  # Accessing updated value by key

null_dict = {}  # Creating an empty dictionary
print(null_dict)  # Output: {}

#Nested Dictionary
nested_dict = {
    
        "name":"Fajar",
        "age":18,
        "subjects":{
            "subject1":"Python",
            "subject2":"C++",
            "subject3":"SQL"
        }
}

print(nested_dict)  # Output: {'student1': {'name': 'Fajar', 'age': 18, 'subjects': {'subject1': 'Python', 'subject2': 'C++', 'subject3': 'SQL'}}}
print(nested_dict["subjects"]["subject1"])  # Accessing nested value by keys
print(nested_dict["subjects"]["subject2"])  # Accessing nested value by keys

#Dictionary Methods
print(nested_dict.keys())
print(list(nested_dict.keys()))  # Convert keys to a list
print(len(mydict))

#value function
print(nested_dict.values())  # Get all values in the dictionary
print(list(nested_dict.values()))  # Convert values to a list

#,items method
print(nested_dict.items())  # Get all key-value pairs in the dictionary
print(list(nested_dict.items()))  # Convert items to a list of tuples

# Adding a new key-value pair
student={
    "name": "Fajar",
    "age": 18,
    "subjects":{
        "OOP":78.8,
        "SQL": 89.5,
        "Python": 95.0
    }
}

# print(student["name2"]) #Error output because "name2" key does not exist
print(student.get("name2"))  # Using get method to avoid error, returns "Key not found" #output will be error

#update method
student.update({"city": "lahore", "Blood group": "B-"})  # Adding a new key-value pair
print(student)

# Removing a key-value pair
del student["age"]  # Deleting the "age" key-value pair
print(student)

