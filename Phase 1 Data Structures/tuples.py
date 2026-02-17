# What is a tuple?
# A tuple is an ordered collection of elements.
# It is usually immutable, meaning its values cannot be changed after creation.
# Tuples can store different data types (e.g., numbers, strings, booleans).
# They are commonly used to group related data together.
# In languages like Python, tuples are written using parentheses, e.g., (1, "apple", True).

# Why Use Tuple Instead of List?

# When data should not change
# Faster than list
# Can be used as dictionary keys
# Safer data structure

# Creating a Tuple
my_tuple = (1,2,3,4,5,6,7,8,9,10)
print(my_tuple)

fruits = ("apple", "banana", "cherry","date", "elderberry")
print(fruits)

mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple)

single_element_tuple = (42,)  # Note the comma to create a single-element tuple
print(single_element_tuple)


# Operations on Tuples
# Accessing Elements
print("----------------------------------------------------------------------")
print(my_tuple[0])  # Accessing the first element (index 0)
print(fruits[1])  # Accessing the second element (index 1)
print(my_tuple[-1])  # Accessing the last element using negative indexing

# Slicing
print("----------------------------------------------------------------------")
print(my_tuple[4:10])  # Slicing from index 4 to the end of the tuple
print(fruits[1:5])

# Concatenation
print("----------------------------------------------------------------------")
frist_tuples = (1,2,3,4,5)
second_tuple = (6,7,8,9,10)

concatenated_tuple = frist_tuples + second_tuple
print(concatenated_tuple)

# Repetition
print("----------------------------------------------------------------------")
repetition_tuple = (1,2,3)
print(repetition_tuple * 3)  # Repeats the tuple three times

# Membership Test
print("----------------------------------------------------------------------")
membership_tuples = (1,2,3,4,5)
print(2 in membership_tuples) 
print(6 in membership_tuples)

# Iteration
print("----------------------------------------------------------------------")
tuple_iteration = (1,2,3,4,5)
for element in tuple_iteration:
    print(element)

# Tuple Functions
print("----------------------------------------------------------------------")
tuple = (1,2,3,4,5)
print(len(tuple))  # Length of the tuple
print(max(tuple))  # Maximum value in the tuple 
print(min(tuple))  # Minimum value in the tuple
print(sum(tuple))  # Sum of all elements in the tuple
print(tuple.count(2))  # Count of the value 2 in the tuple

