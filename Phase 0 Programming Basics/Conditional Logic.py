# What Are Conditions?
# Conditions allow programs to make decisions.

# if condition:
#     #code
# else:
#     #code

# | Operator | Meaning          |
# | -------- | ---------------- |
# | `==`     | Equal            |
# | `!=`     | Not equal        |
# | `>`      | Greater than     |
# | `<`      | Less than        |
# | `>=`     | Greater or equal |
# | `<=`     | Less or equal    |


age = int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


# Multiple Conditions (elif)

marks = int(input("Enter your marks:"))
if marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

else:
    print("Grade: F")

# Check if a number is positive or negative

number = float(input("Enter a number:"))
if number > 0:
    print("The number is positive")

elif number < 0:
    print("The number is negitive")

else:
    print("The number is zero")


# Check if a person is eligible for driving

age = float(input("Enter your age:"))
if age >= 18:
    print("You are eligible for driving")
else:
    print("You are not eligible for driving yet")

# Find the largest of two numbers
num1  = float(input("Enter frist number:"))
num2 = float(input("Enter second number:"))

if num1 > num2:
    print("The largest number is:", num1)
elif num2 > num1:
    print("The largest number is:", num2)
else:
    print("Both numbers are equal.")

# Find the largest of three numbers

num1 = float(input("Enter frist number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))

if num1 == num2 and num2 == num3:
    print("All three numbers are equal.")
elif num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)

# Check if a number is divisible by 5
number = int(input("Enter a number:"))
if number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")

# Check if a year is a leap year
year = int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
