# This is for quickly testing blocks of code

# for number in range(1,6):
#     print(number)

# for number in range(3):
#     print("Attempt", number)

# message = "Hello, world!"

# for character in message:
#     print(character)

# for number in range(1,10):
#     if (number % 2 == 0):
#         print(number)

# total = 0
# numbers = [1,3,5,9,2]
# for number in numbers:
#     total += number
# print(total)

# outer_count = 5

# while outer_count > 0:
#   # Outer loop controls the number of times the inner loop runs
#   inner_count = 1
#   while inner_count <= outer_count:
#     # Inner loop repeats for each outer loop iteration
#     print(inner_count, end=" ")
#     inner_count += 1
#   print()  # Move to a new line after each outer loop iteration
#   outer_count -= 1

# for i in range(1, 11):
#   # Outer loop iterates through rows (multiplication factors)
#   for j in range(1, 11):
#     # Inner loop iterates through columns (other factors)
#     product = i * j
#     print(f"{j} x {i} = {product}", end="\t")  # Print with tabs for better formatting
#   print()  # Move to a new line after each row

# rows = 5

# for i in range(1, rows + 1):
#   # Outer loop controls the number of rows
#   for j in range(1, i +1):
#     # Inner loop prints asterisks for each row
#     print("*", end="")
#   print()  # Move to a new line after each row of asterisks


# weight = float(input("Enter your weight: "))
# unit = input("(K) for Kilograms and (L) for Pounds: ").upper()
# if unit == "K":
#     converted_weight = round((weight * 2.205), 2)
#     print(f"Your weight is {converted_weight} in pounds")
# elif unit == "L":
#     converted_weight = round((weight / 2.205), 2)
#     print(f"Your weight is {converted_weight} in kilograms")
# else:
#     print("Enter correct unit")
    
# def greet(name = "World"):
#     print(f"Hello, {name}")

# greet("Timi")
# greet()

# add = lambda x,y: x+y
# result = add(5,3)
# print(result)

# def area(length, breadth):
#     return length * breadth

# print(area(20, 5))

# def numberCheck(number):
#     if number % 2 == 0:
#         print(f"{number} is an even number")
#     elif number % 2 == 1:
#         print(f"{number} is an odd number")
#     else:
#         print("Enter an integer")

# numberCheck(6)
# numberCheck(5)
# numberCheck(4.2)

# fruits = ["orange", "mango", "pineapple", "apple", "watermelon"]
# for i in fruits:
#     print(i)



# fav_book = {"Title":"Rich Dad Poor Dad", "Author":"Robert Kiyosaki", "Genre":"Finance"}
# print(fav_book["Genre"])

# from Calculator import multiply as mult

# mult(5,2)

# import requests

# requests.get()