# What is a Set in Python?
# A set in Python is a built-in data type used to store multiple unique elements in a single variable.
# Sets are unordered
# Sets do not allow duplicate values
# Sets are mutable (you can add or remove items)
# Sets are written using curly brackets {}

my_set = {1,2,3,4,5}
print(my_set)

numbers = {1,2,2,3,3,4}
print(numbers)

# Why Are Sets Useful?
# Removing duplicates

# Fast membership testing
fruits = {"apple","banana","cherry"}
print("banana" in fruits)

# Mathematical operations
# Sets support union, intersection, difference, etc.

# union operations
A = {1,2,3}
B={3,4,5}

print("Union operaions ->",A.union(B))

# Intersection operations
A = {1,2,3,4}
B={3,4,5}

print("Intersection operations ->", A.intersection(B))

#Difference operations
A = {1,2,3,4}
B = {3,4,5}
print("Difference operations ->", A - B)
print("Difference operations ->", B - A)

#Symmetric Difference
A = {1,2,3,4}
B = {3,4,5}
print("Symmetric Difference ->", A ^ B)

# Practice Problems - Sets
# Create a set of integers
set_int = {1,2,3,4,5}
print("Set of the integers ->" , set_int)

#Remove duplicates from a list using a set
remove_duplicates = {1,2,2,3,3,4}
print("Remove duplicates ->", remove_duplicates)

# Find common elements between two sets
common_elements = {1,2,3,4}
other_set = {3,4,5,6}

print("Common elements ->", common_elements.intersection(other_set))

# Find unique elements in two lists
list_frist = [1,2,3,4]
list_second = [3,4,5,6]

print("Unique elements ->", set(list_frist) .union(set(list_second)))

# Add and remove elements from a set
my_set = {1,2,3}
my_set.add(4)
print("After adding an element ->", my_set)
my_set.remove(2)
print("After removing an element ->", my_set)

# Check if a value exists in a set
my_set = {1,2,3,4,5}
print("Check if 3 exists in the set ->", 3 in my_set)
print("Check if 6 exists in the set ->", 6 in my_set)

# Find students enrolled in both courses
course_a = {"Alice", "Bob", "Charlie"}
course_b = {"Charlie", "David", "Eve"}

print("Students enrolled in both courses ->", course_a.intersection(course_b))

# Convert set to list
my_set = {1,2,3,4,5}
my_list = list(my_set)
print("Set converted to list ->", my_list)

# Find difference between two sets
set_a = {1,2,3,4}
set_b = {3,4,5,6}
print("Different between two sets ->", set_a - set_b)
print("Different between two sets ->", set_b - set_a)

# Create a set from user input
user_input = input("Enter numbers separated by commas: ")
user_set = set(map(int, user_input.split(",")))
print("Set created from user input ->", user_set)