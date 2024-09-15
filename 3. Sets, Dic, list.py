# Assignment 1: Develop a Python program that performs various data analysis tasks on a dataset represented as a list of tuples. Each tuple contains information about a student, including their name, age, and scores in three subjects.
# Input Data:
# Prompt the user to enter data for multiple students. Each student’s data should include their name (string), age (integer), and scores in three subjects (integers).
# Store this data as a list of tuples, where each tuple represents a student in the format: (name, age, score1, score2, score3).

# students_data = []
# new_stud_data = []
#
# while True:
#     choice = int(input("To add a student enter 1, to calculate average scores enter 2, to find highest average enter 3, "
#                        "to find students above average of averages enter 4, and to exit enter 0: "))
#     match choice:
#         case 1:
#             name = input("Enter the name of the student: ")
#             age = int(input("Enter the age of the student: "))
#             score1 = int(input("Enter score in first subject: "))
#             score2 = int(input("Enter score in second subject: "))
#             score3 = int(input("Enter score in third subject: "))
#
#             stud_tup = (name, age, score1, score2, score3)
#             students_data.append(stud_tup)
#
#         case 2:
#             for student in students_data:
#                 name, age, score1, score2, score3 = student
#                 average = (score1 + score2 + score3) / 3
#                 updated_tup = (name, age, score1, score2, score3, average)
#                 new_stud_data.append(updated_tup)
#
#             print("Student data with averages:", new_stud_data)
#
#         case 3:
#             highest_score = -1
#             highest_name = ""
#             for stu in new_stud_data:
#                 if stu[-1] > highest_score:
#                     highest_score = stu[-1]
#                     highest_name = stu[0]
#
#             if highest_name:
#                 print(f"Highest average score is {highest_score} by {highest_name}")
#             else:
#                 print("No valid highest average found.")
#
#         case 4:
#             total_sum = 0
#             count = len(new_stud_data)
#
#             for stu in new_stud_data:
#                 total_sum += stu[-1]
#
#             avg_of_averages = total_sum / count if count > 0 else 0
#             print(f"Average of all student averages (passing marks): {avg_of_averages}")
#
#             print("Students with scores above the passing marks:")
#             for stu in new_stud_data:
#                 if stu[-1] > avg_of_averages:
#                     print(f"{stu[0]} with an average score of {stu[-1]}")
#
#         case 0:
#             print("Exit")
#             print("Student data:", students_data)
#             break
#
#         case _:
#             print("Invalid choice, please enter 1, 2, 3, or 0.")


# Assignment 2: Write a program that finds and returns the common elements between two tuples.
# Input:
# Prompt the user to enter two tuples.
# Logic:
# Find the common elements between the two tuples using set operations.
# Return a tuple containing the common elements.
# Output:
# Display the tuple of common elements.

# tup1 = eval(input("Enter tuple 1: "))
# tup2 = eval(input("Enter tuple 2: "))
#
# print(set(tup1).intersection((set(tup2))))

# Assignment 3: Extract unique letter from a given text using sets.
# Input:
# Prompt the user to enter a paragraph of text.
# Logic:
# Split the text into words.
# Convert the list of words into a set to remove duplicates.
# Sort the set alphabetically.
# Output:
# Display the unique words in alphabetical order.
#
# Quick brown fox jumps over the lazy dog

# str1 = "Quick Brown Fox Jumps over the lazy dog".upper()
#
# list1 = str1.replace(" ", "")
#
# set1 = set(list1)
#
# sorted_list = sorted(set1)
# str2 = ''.join(sorted_list)
#
# print(sorted_list)
# print(len(str2))
# print(str2)

# Assignment 4: Simulate Venn diagram-like operations using Python sets.
# Input:
# Create three sets representing different groups of items (e.g., fruits, vegetables, and grains).
# Logic:
# Calculate the following:
# Items common to all three sets (Intersection).
# Items not common to any of the three sets (Symmetric Difference).
# Items unique to each set. (Difference)
# Output:
# Display the results of each operation.

# vegetables = {"Carrot", "Broccoli", "Spinach", "Potato", "Onion"}
# fruits = {"Apple", "Banana", "Spinach", "Orange", "Potato"}
# grains = {"Rice", "Wheat", "Oats", "Barley", "Potato"}
#
# print("Common in all three sets: ")
# print(set.intersection(vegetables,fruits,grains))
# # print(set.intersection(vegetables,fruits) or set.intersection(vegetables,grains) or set.intersection(grains,fruits))
#
# print("item common in two but not in third: ")
# print(vegetables&fruits-grains or fruits&grains-vegetables or grains&vegetables-fruits)
# # print(set.symmetric_difference(vegetables,fruits) or set.symmetric_difference(vegetables,grains) or set.symmetric_difference(grains,fruits))
#
# print("Items unique from all sets: ")
# print(vegetables-fruits-grains | fruits-grains-vegetables | grains-vegetables-fruits)

# Assignment 4: Simulate Venn diagram-like operations using Python sets.
# Input:
# Create three sets representing different groups of items (e.g., fruits, vegetables, and grains).
# Logic:
# Calculate the following:
# Items common to all three sets (Intersection).
# Items not common to any of the three sets (Symmetric Difference).
# Items unique to each set. (Difference)
# Output:
# Display the results of each operation.

# dict = {}
# for i in range(1,6):
#     dict[i] = i ** 3
#
# print(dict)

# Assignment 5 : Create a dictionary where keys are integers from 1 to 5 and values are their cubes

# dict = {}
# for i in range(ord('a'), ord('f')):
#     dict[chr(i)] = i
#
# print(dict)

# Assignment 6 : Generate a dictionary with letters 'a' to 'e' as keys and their ASCII values as values

# dict = {}
# for i in range(ord('a'), ord('f')):
#     dict[chr(i)] = i
#
# print(dict)

# Assignment 7: Develop a program to manage an inventory system for a small store.
# Input:
# Prompt the user to enter items, their quantities, and prices.
# Store the data in a dictionary where keys are item names, and values are another dictionary containing quantity and price.
# Logic:
# Implement functions to:
# Add new items to the inventory.
# Update the quantity or price of existing items.
# Calculate the total value of the inventory (sum of all items' value = quantity * price).
# Output:
# Display the current inventory.
# Display the total value of the inventory.

# inverntory = {}
#
# while True:
#     choice = int(input("Enter 1 to add a new item, 2 to calculate total sum of all item and 0 to exit: "))
#     match choice:
#         case 1:
#             item = input("Enter the name of the item: ")
#             quantity = int(input("Enter the quantity: "))
#             price = int(input("Enter the price of the item: "))
#             inverntory[item] = {"Quantity": quantity, "Price": price}
#             print(inverntory, end="\n")
#
#         case 2:
#             sum = 0
#             for key, value in inverntory.items():
#                 qty, price = value["Quantity"], value["Price"]
#                 # sum += inverntory[key][0] * inverntory[key][1]
#                 sum += qty * price
#             print(f"The total value of inventory = {sum}", end="\n")
#
#         case 3:
#             item = input("Enter the name of the item: ")
#             quantity = int(input("Enter the quantity: "))
#             price = int(input("Enter the price of the item: "))
#             update_item = {item:{"Quantity": quantity, "Price": price}}
#             inverntory.update(update_item)
#
#         case 4:
#             print("Exiting...")
#             break
#
#         case _:
#             print("Enter valid choice from 1,2,3 only")

# Assignment 12 : Given a dictionary, invert it such that keys become values and values become keys.
# Input: Use the dictionary {'a': 1, 'b': 2, 'c': 3}.
# Logic: Use a dictionary comprehension to swap keys and values.
# Output: Display the inverted dictionary.

# dictionary = {'a': 1, 'b': 2, 'c': 3}
#
# new_dict = {value: key for key, value in dictionary.items()}
#
# print(new_dict)

