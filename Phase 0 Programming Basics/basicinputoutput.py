# print("Inside the basic input output file")
# name = input("Enter your name:")
# age = input ("Enter your  age:")

# print("Welcome", name, "and you are", age, "years old")

# Practice Problems (Input/Output)

# Question 1: Ask the user for their name and greet them
user_name = input("What is your name?")
print("Hello,", user_name + " Good to meet you!")


# Question 2: Ask for two numbers and print their sum
num1 = float(input("Enter frist number:"))
num2 = float(input("enter second number:"))

sum = num1 + num2
print("Sum of the numbers is", sum)

# Take a user's age and print how old they’ll be after 10 years
current_user_age = int(input("Enter your current age:"))
age_after_10_years = current_user_age + 10
print("Your age after 10 years will be:", age_after_10_years)

# Ask for a city name and print it in uppercase
city_name = input("Enter your city name:")
print("City name in the upper case is:", city_name.upper())

# Ask for a number and print its square
number = float(input("Enter a number to find it's square:"))
square = number ** 2
print("The square of the number is:", square)