# Get user input
num = int(input("Enter a number: "))

# Input three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Find the largest number
largest = max(num1, num2, num3)
print(f"The largest number is: {largest}")

# Input a number for which the table is needed
num = int(input("Enter a number: "))

# Print the multiplication table
print(f"Multiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")
