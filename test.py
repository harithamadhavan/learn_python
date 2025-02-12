# Input list and element to check
fruits = ["apple", "banana", "cherry", "date"]
item = input("Enter fruit name to check: ")

# Check if item is in the list
if item in fruits:
    print(f"{item} is in the list.")
else:
    print(f"{item} is not in the list.")
