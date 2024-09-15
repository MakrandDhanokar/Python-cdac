# Assignment 1: Dynamic Sum Calculator
# Objective: Write a function that takes a variable number of numerical arguments and returns their sum.
# Tasks:
# Implement a function ‘sum_numbers(*args)’ that calculates the sum of all arguments passed to it.
# Ensure the function can handle any number of arguments.
# Challenge: Modify the function to exclude negative numbers from the sum.

# def addition(*args):
#     return sum(args)
# print(addition(1, 2, 3, 4))

# Assignment 2: Dynamic Report Generator
# Objective: Create a function that generates a report in a structured format, based on variable arguments and keyword arguments.
# Tasks:
# Write a function generate_report(title, *args, **kwargs)
# title is the report title
# *args are the report sections
# **kwargs contain additional metadata like author, date, etc.
# Sample Input to function generate_report :
# ("Monthly Sales Report", "Introduction: Overview of sales performance.", "Data Analysis: Breakdown of sales data by region.", "Market Trends: Analysis of current market trends.", author="John Doe", date=“September 2024", conclusion="Overall, sales have increased by 15% compared to the previous month.", skip_sections=[2])
# Challenge: Add the ability to include optional sections or skip sections based on keyword arguments.

# def generate_report(title, *args, **kwargs):
#     sections = args
#     metadata = kwargs
#
#     print("\t\t\t\t\t", title)
#     print("=============================================================")
#
#     for key, value in metadata.items():
#         if key in ("author", "date"):
#             print(f"{key.capitalize()}: {value}")
#     print("=============================================================")
#     print("\nReport Sections:")
#     print("----------------")
#     for i, section in enumerate(sections, start=1):
#         if i in metadata.get("skip_sections", []):
#             continue
#         print(f"Section {i}: {section}")
#
#     print("\n")
#     for key, value in metadata.items():
#         if key == "conclusion":
#             print(f"{key.capitalize()}")
#             print("----------")
#             print(value)
#
#
# generate_report(
#     "Monthly Sales Report",
#     "Introduction: Overview of sales performance.",
#     "Data Analysis: Breakdown of sales data by region.",
#     "Market Trends: Analysis of current market trends.",
#     author="John Doe",
#     date="September 2024",
#     conclusion="Overall sales have increased by 15% compared to the previous month",
#     skip_sections=[2]
# )

# Assignment 3: Global and Local Summation
# Objective: Create a program that calculates the sum of numbers using both global and local variables.
# Tasks:
# Declare a global variable to store the sum of numbers.
# Write a function that accepts a list of numbers and calculates the sum using a local variable.
# Update the global sum variable with the local sum calculated in the function.
# Print the global sum before and after calling the function.
# Challenge: Implement another function that resets the global sum to zero and compare the results.

# addition_global = 0
#
# def add(*args):
#     global addition_global
#     add1 = sum(args)
#     addition_global += add1
#     return add1
#
# def reset_global_sum():
#     global addition_global
#     addition_global = 0
#     print(addition_global)
#
# print(f"local sum: {add(1,2,3)}")
# print(f"Global sum is updated to: {addition_global}")
# print(f"local sum: {add(1,2,3)}")
# print(f"Global sum is updated to: {addition_global}")
# print(f"local sum: {add(1,2,3)}")
# print(f"Global sum is updated to: {addition_global}")
#
# print(f"Global sum is reset to:", end=" ")
# reset_global_sum()

# Assignment 4: Global Counter
# Objective: Create a function that uses a global variable to count the number of times the function has been called.
# Tasks:
# Declare a global counter variable outside of the function.
# Each time the function is called, increment the counter and print the current count.
# Challenge: Modify the function to allow resetting the counter using an optional argument.

# Assignment 5: Conditional Lambda Functions
#
# Objective: Create a program that uses a lambda function to check if a number is positive, negative, or zero.
#
# Tasks:
# Input: List of integers. E.g. numbers = [10, -5, 0, 7, -3, 4, -2]
# Logic: Use the map() function with a lambda function to return "Positive", "Negative", or "Zero" based on the value of each integer.
# Output: Display the resulting list of strings.
# 	E.g. : ['Positive', 'Negative', 'Zero', 'Positive', 'Negative', 'Positive', 'Negative']

# cube = lambda X: X*X*X
# print(f"Cube: {cube(3)}")
#
# numbers = [10, -5, 0, 7, -3, 4, -2]
# result = map(lambda x: "positive" if x > 0 else ("negative" if x < 0 else "zero"), numbers)
#
# print(numbers)
# print(list(result))

# Assignment 6: Convert factorial program to use recursive functions

# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     return num * factorial(num-1)

# Assignment 7: Define functions which handle exceptions
# Function 1:  get_integer_input – Accepts an integer and prints it
# Exception to handle : ValueError exceptions
# Function 2: get_element_from_list - Attempts to return element at specified index from list.
# Exceptions to handle :
# IndexError : if the index is out of bounds
# TypeError if the index is not an integer
# Use else : Print the element if no exceptions occur
# finally blocks : to indicate operation completion
# Function3: divide_numbers(a, b) - Raises ZeroDivisionError if b is zero
# Exception to handle : ZeroDivisionError - Custom message in body

# def get_element_from_list(li, n):
#     """"This is a function to get an integer from a list"""
#     try:
#         element = li[n]
#     except IndexError as e:
#         print(f"{e}")
#     except TypeError as e:
#         print(f"{e}")
#     else:
#         print(element)
#     finally:
#         print("Program completed")
#
#
# get_element_from_list([1, 2, 3, 4], "str")
# print(__doc__)
# print(get_element_from_list.__doc__)

# Assignment 8 : Add ‘docStrings’ to exception handling assignment
# Assignment 9: Store report generated in Assignment 2 to a text file.

# def generate_report(title, *args, **kwargs):
#     sections = args
#     metadata = kwargs
#
#     with open('report.txt', mode='w') as file:
#         file.write(f"\t\t\t\t\t {title}")
#         file.write("\n=============================================================")
#
#
#         for key, value in metadata.items():
#             if key in ("author", "date"):
#                 file.write(f"\n{key.capitalize()}: {value}")
#         file.write("\n=============================================================")
#         file.write("\nReport Sections:")
#         file.write("\n----------------")
#         for i, section in enumerate(sections, start=1):
#             if i in metadata.get("skip_sections", []):
#                 continue
#             file.write(f"\nSection {i}: {section}")
#
#         file.write("\n")
#         for key, value in metadata.items():
#             if key == "conclusion":
#                 file.write(f"\n{key.capitalize()}")
#                 file.write("\n----------\n")
#                 file.write(value)
#
#
# generate_report(
#     "Monthly Sales Report",
#     "Introduction: Overview of sales performance.",
#     "Data Analysis: Breakdown of sales data by region.",
#     "Market Trends: Analysis of current market trends.",
#     author="John Doe",
#     date="September 2024",
#     conclusion="Overall sales have increased by 15% compared to the previous month",
#     skip_sections=[2]
# )
#
# with open('report.txt', mode='r') as file:
#     contents = file.read()
#
# print(contents)

# Assignment 10: Replace a Keyword in a Text File
# Search for all occurrences of keyword 'after', replace it with 'before’. Save modified content back to file.
# Create functions wherever appropriate.
# Handle the exception
# FileNotFoundError

# str1 = input("Enter a sentence")
#
# with open("Input.txt", mode='w') as file1:
#     file1.write(str1)
# file1.close()
#
# with open("Input.txt", mode='r') as file2:
#     contents = file2.read()
# print(contents)
# file2.close()
#
# with open("Input.txt", mode='w') as file3:
#     file3.write(contents.replace('after', 'before'))
# file3.close()
#
# with open("Input.txt", mode='r') as file2:
#     contents = file2.read()
# print(contents)
# file2.close()

# Assignment 11: Writing Data to a CSV File
# Define Data:
# Create a list of dictionaries where each dictionary represents a student's record with the following fields:
# ID, Name, Age, Grade
# Instructions:
# Use the csv module to write the list of dictionaries to a CSV file named students.csv.
# The CSV file should have headers based on the dictionary keys: ID, Name, Age, and Grade.
# Ensure that each record is written to a new row in the CSV file.
# Function Definition:
# Function 1: write_students_to_csv(filename: str, student_list: list)
# Use the csv.DictWriter class to write the dictionaries to the CSV file.
# Make sure to include a header row with the keys of the dictionaries.
# Function 2: read_csv_and_print(filename: str)

# stud_dict = {}
# while True:
#     choice = int(input("Do you want to add a student press 1, else 0"))
#     match choice:
#         case 1:
#             id = int(input("Enter the id: "))
#             name = input("Enter the name: ")
#             age = int(input("Enter the age: "))
#             grade = input("Enter the grade: ")
#             stud_dict.update({id: {"name": name, "age": age, "grade": grade}})
#
#         case 0:
#
#             with open("student.csv", mode='a') as file:
#                 file.write(str(f"{stud_dict}\n", ))
#                 print("Exiting")
#             break

# Assignment 12: Merging Files
# Create a Python program that merges the contents of multiple text files into a single list, removes duplicate lines, and saves the unique lines to a new file.
# Input: Two or more text files, each containing several lines of text.
# Logic:
# Read the content of each file into separate lists.
# Merge the lists into a single list.
# Convert the list to a set to remove duplicate lines.
# Write unique lines to a new file named merged_unique.txt.
# Output: Display the merged list and confirm that the unique lines have been saved.

# import csv
#
#
# def read_csv(file_name):
#     with open(file_name, mode='r') as file:
#         reader = csv.reader(file)
#         return list(reader)
#
#
# def write_csv(file_name, data):
#     with open(file_name, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)
#
#
# data1 = read_csv('students1.csv')
# data2 = read_csv('students2.csv')
#
# combined_data = data1 + data2
#
# unique_data = list(set(tuple(row) for row in combined_data))
#
# unique_data = [list(row) for row in unique_data]
# unique_data.sort()
#
# write_csv('unique_students.csv', unique_data)
#
# print("Unique CSV file created successfully.")
