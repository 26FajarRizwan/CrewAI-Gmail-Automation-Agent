dictionary={
    "cat": "a small animal",
    "table": ["a piece of furniture", "a place to eat"]
}

print(dictionary)

subjects={
    "python","java", "c++", "javascript","java",
    "python","java","c++","c"
}
print(len(subjects))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

marks={

}
x=input("Enter marks for subject 1: ")
marks.update({"subject1": x})

y=input("Enter marks for subject 2: ")
marks.update({"subject2": y})

z=input("Enter marks for subject 3: ")
marks.update({"subject3": z})

print(marks)

# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

values={9,9.0}
print(values) #9and9.0 are considered the same in a set, so they will not be stored separately.

# To store them separately, we can use a list or a tuple instead of a set.
values_list = [9, 9.0]
print(values_list)  # This will store both 9 and 9.0 separately.

#also by saving one in string and one in integer
values_set = {9, "9.0"}
print(values_set)  # This will store 9 as an integer and "9.0" as a string.

values_dict={
    ("float", 9.0),
    ("int", 9)
}
print(values_dict)  # This will store both as a tuple in a dictionary-like structure.654
