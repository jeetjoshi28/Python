# In Python, a list is a built-in data type used to store multiple values in a single variable.
# Lists are ordered, meaning items have a fixed position and can be accessed by index.
# They are mutable, so you can change, add, or remove elements after creation.
# A list can hold different data types like numbers, strings, or even other lists.
# Lists are created using square brackets [].
# Example: my_list = [1, "apple", 3.5]

numbers = [10,20,30,40,50]
print(numbers)

#List Operations
#1 Accessing Elements
# List elements are accessed using an index. Indexing starts from 0 for the first element.
print(numbers[2])  # Accessing the third element (index 2)

#2 Adding Elements 
numbers.append(60)
print("Append the values in the list:",numbers)

#3 Adding the Elements at a specific positions
numbers.insert(2,70)
print("Add the value at the specific position:",numbers)

#4 This is is incorrect way to add the element at specific position
# numbers.append(3,90)
# print("Add the value at the specific position using append:",numbers)

#5 Removing Elements
# Elements can be removed using methods like remove() (removes a specific value) or pop() (removes by index or last element).
numbers.remove(30)  # Remove the value 30 from the list
print("Remove the specific value from the list:",numbers)

numbers.pop(1)  # Remove the element at index 1 (which is 20)
print("Remove the element at specific index from the list:",numbers)

#6 Updating Elements
# Since lists are mutable, their values can be changed by assigning a new value to a specific index.
numbers[0] = 15  # Update the first element to 15
print("Update the value at specific index in the list:",numbers)

#7 Slicing
# Slicing allows you to access a range of elements in a list. The syntax is list[start:end], where start is the index to begin slicing (inclusive) and end is the index to end slicing (exclusive).
print(numbers[1:4]) 

#8 Length of List
print("Length of the list is:", len(numbers))

#9 Mebership Test
print("Is 40 in the list?", 40 in numbers)
print("Is 90 in the list?", 90 in numbers)

#10 Sorting Operations
numbers.sort()
print("Sorted list:", numbers)

#11 Reverse the list
numbers.reverse()
print("Reversed list:", numbers)

#12 Copying a list
copied_list = numbers.copy()
print("Copied list:", copied_list)

#13 Nested Lists
nested_list = [1,2,[3,4],5]
print("Nested list:", nested_list)

names = ["Alice","Bob","Charlie"]
print(names)
print(names[1])

# Practice Problems
# Create a list of 5 integers and print them
name_list = ["Jeet","Rahul","Sita","Gita","Ravi"]
print(name_list)

# Find the sum of all elements in a list
sum_of_list = [10,20,30,40,50]
print("Sum of the list is:", sum(sum_of_list))

# Find the largest and smallest number in a list
max_min = [10,20,30,40,50]
print("Largest number in the list is:", max(max_min), "Minimum number in the list is:", min(max_min))

# Count how many times a number appears
repeated_num_list = [1,2,3,2,4,2,5,3]
print("Count of 2 in the list is:", repeated_num_list.count(2))
print("Count of 3 in the list is:", repeated_num_list.count(3))

# Reverse a list without using .reverse()
reversed_list = []
for i in range(len(repeated_num_list) - 1, -1, -1):
    reversed_list.append(repeated_num_list[i])
print("Reversed list without using .reverse():", reversed_list)
# Remove duplicate values from a list
uniq_list = [1,2,3,2,4,2,5,3]
print("Original list with duplicates:", uniq_list)
unique_values = list(set(uniq_list))
print("List after removing duplicates:", unique_values)

# Merge two lists
list_one = [1,2,3]
list_two = [4,5,6]
merged_list = list_one + list_two
print("Mearged list:", merged_list)

name = ["Jeet"]
sarname = ["Joshi"]
full_name = name + sarname
print("full name is:" , full_name)

# Check if an element exists in a list
exiting = [1,2,3,4,5]
print("Is 3 in the list?", 3 in exiting)
print("Is 6 in the list?", 6 in exiting)
# Create a list of even numbers from 1 to 50
even_num = [num for num in range(1,51) if num % 2 == 0]
print("List of the even numbers upto 50:", even_num)

# Sort a list in descending order
descending_list = [10,30,20,50,40]
descending_list.sort()
print("Sorted list in ascending order:", descending_list)
descending_list.reverse()
print("Sorted list in descending order:", descending_list)

# second way to sort a list in descending order
descending_list_2 = [10,30,20,50,40]
descending_list_2.sort(reverse=True)
print("Sorted list in descending order using sort with reverse:", descending_list_2)