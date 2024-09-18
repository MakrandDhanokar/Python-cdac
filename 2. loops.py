# Assignment 1: Write a program to calculate the sum of the digits of a given positive integer.
# Input: Prompt the user to enter a positive integer.
# Logic: Use a for loop to iterate through each digit of the number and calculate the sum.
# Output: Display the sum of the digits.

# num = int(input("Enter a number here: "))
# sum = 0
# while num > 0:
#     sum = sum + int(num%10)
#     num = int(num/10)
#
# print(f"The sum of the number is {sum}")

# ------------------------------------------------------------------------------------------------------------------------

# Assignment 2:  Write a program to generate and display the multiplication table of a given number up to 12.
# Input: Prompt the user to enter a number.
# Logic: Use a for loop to calculate and display the multiplication table for the number.
# Output: Display the multiplication table

# num = int(input("Enter a number here: "))
# for i in range(1, 13):
#     print(f"{num} X {i} = {num*i}")
# print(end='\n')

# ------------------------------------------------------------------------------------------------------------------------

# Assignment 3: Develop a program that simulates an ATM withdrawal process.
# Input: Prompt the user to enter their account balance and the amount they wish to withdraw.
# Logic:
# Check if the withdrawal amount is greater than the account balance. If so, display an error message.
# If the withdrawal amount is valid, subtract it from the balance.
# Ensure the withdrawal amount is a multiple of 10 (as ATMs typically dispense money in multiples of 10).
# Output:
# Display the remaining balance if the withdrawal is successful.
# If not, display an appropriate error message (e.g., "Insufficient balance" or "Amount must be a multiple of 10").
# Check if user wishes to withdraw more money, else exit

# balance = int(input("Enter your Account balance: "))
#
# choice = True
# while(choice):
#     print("***********************************************")
#     withdraw = int(input("Enter the amount to withdraw: "))
#     if(withdraw%10!=0):
#         print("Enter the amount multiple of 10")
#         continue
#     if(balance<withdraw):
#         print("Error: Insufficient funds")
#         break
#     else:
#         balance = balance - withdraw
#         print(f"your available balance is {balance}\n")
#         print("***********************************************")
#         choice = int(input("Do you want to continue: Press 1\n"))
#
# balance = int(input("Enter your Account balance: "))
#
# choice = True
# while(choice):
#     print("***********************************************")
#     withdraw = int(input("Enter the amount to withdraw: "))
#     if(withdraw%10!=0):
#         print("Enter the amount multiple of 10")
#         continue
#     if(balance<withdraw):
#         print("Error: Insufficient funds")
#         break
#     else:
#         balance = balance - withdraw
#         print(f"your available balance is {balance}\n")
#         print("***********************************************")
#         choice = int(input("Do you want to continue: Press 1\n"))

# ------------------------------------------------------------------------------------------------------------------------

# Assignment 4:
# Create Multiplication tables for 1 – 5 numbers using nested for loops

# for i in range(1, 11):
#     for j in range(1, 6):
#         print(f"{j} X {i} = {i * j}", end="\t\t")
#     print("")

# ------------------------------------------------------------------------------------------------------------------------

# Assignment 5 : Write a program to generate and display a triangular pattern of numbers based on user input using nested while loop
# Input:
# Prompt the user to enter the number of rows for the pattern (e.g., 4 for a pattern with 4 rows).
# Output:
# The program should display the pattern in a triangular format. For example, if the user inputs 5, the output should look like this:

# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print(end='\n')
# ------------------------------------------------------------------------------------------------------------------------

# Assignment 6: Create a calculator for performing addition, subtraction, division, multiplication operations using match-case.
# Input :
# Ask user what operation needs to be performed.
# Ask user if next operation needs to be performed. Based on the answer repeat same steps or exit.

# operation = input("Enter any operation: ")
#
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# out = 0
#
# match operation:
#     case "addition":
#         out = num1 + num2
#     case "subtraction":
#         out = num1 - num2
#     case "multiplication":
#         out = num1 * num2
#     case "division":
#         out = num1 / num2
#     case _:
#         print("wrong input")
#
# print(out)

# Assignment 8: Create a program that generates and stores all prime numbers up to a given number in a list.
# Input:
# 	Prompt the user to enter a positive integer n.
# Logic:
# Write a function that checks if a number is prime.
# Use a loop to generate all prime numbers up to n and store them in a list.
# Output:
# 	Display the list of prime numbers.

# import math
# num = int(input("Enter a number: "))
# prime_numbers = []
#
# for i in range(2, num+1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         prime_numbers.append(i)
#
# print(prime_numbers)

# Assignment 9 : Write a program that implements a basic to-do list where users can add, remove, and view tasks.
# Input:
# Allow the user to add tasks to the to-do list.
# Allow the user to remove tasks by specifying the task name.
# Allow the user to view the current list of tasks.
# Logic:
# Use a list to store the tasks.
# Implement a loop that continuously prompts the user to choose an action (add, remove, view, or exit).
# Output:
# Display the updated to-do list after each operation.

# to_do_list = []
# choice = True
#
# while choice:
#     task = input("Enter the choice from below \n1. Add a entry, \n2. Remove a entry, \n3. View all entries  \n0. To exit \n Enter Your Choice: ")
#     print("****************************************************************************************************************")
#     match task:
#         case "1":
#             to_do = input("Enter the task: ")
#             to_do_list.append(to_do)
#             print(to_do_list)
#         case "2":
#             to_do = input("Enter the task to remove: ")
#             if to_do in to_do_list:
#                 to_do_list.remove(to_do)
#             else:
#                 print(f"{to_do} not in to do list")
#         case "3":
#             print(to_do_list)
#         case _:
#             print("Exiting...")
#             choice = False
#     print("****************************************************************************************************************")

# Assignment 10:  Write a program that rotates a given list to the right by a specified number of positions.
# For e.g. :  If list is [1, 2, 3, 4, 5] and number of positions is 2, then rotated list should be [4, 5, 1, 2, 3].
# Input:
# Prompt the user to enter the elements of the list, separated by spaces or commas (e.g., 1  2  3  4  5).
# Prompt the user to enter the number of positions to rotate the list to the right.
# Calculation:
# Rotate the list to the right by the specified number of positions. If the number of positions exceeds the length of the list, use modulo operation to handle this case.
# Output:
# Display the original list and the rotated list.
# Requirements:
# Ensure that the rotation handles cases where the number of positions is greater than the length of the list.

# str1 = input("Enter the elements of the list: ")
#
# list = str1.split(sep=' ')
# size = len(list)
# list = [int(x) for x in list]
#
# rotations = int(input("Enter the number of rotations: "))
#
# rotations = rotations%size
#
# for i in range(0,rotations):
#     list.insert(0,list.pop(-1))
#
# print(list)

# Assignment 11: Tuple Manipulation
# Input:
# Prompt the user to enter a list of elements separated by commas (e.g., 10, 20, 30, 40, 50).
# Tasks:
# Convert the input string to a tuple of integers.
# Perform the following operations and display the results:
# Print the first element of the tuple.
# Print the last element of the tuple.
# Print tuple excluding first and last elements (slice of tuple from second to second-to-last element).
# Print every second element of the tuple (i.e., slicing with a step).
# Print the tuple reversed (i.e., use slicing to reverse the tuple).
# Output:
# Display results of the above operations in a clear format.

# str1 = input("Enter the elements of the list: ")
#
# tup = tuple(int(x) for x in str1.split(sep=' '))
#
# print(f'First element of tuple is {tup[0]}')
# print(f'Last element of tuple is {tup[-1]}')
# print(f'Tuple excluding first and last element {tup[1:-1]}')
# print(f'Every second element in tuple is {tup[::2]}')
# print(f'Elements in Reverse {tup[::-1]}')

# Assignment 12:  Develop a program that demonstrates tuple packing and unpacking, including nested tuple unpacking.
# Input:
# Prompt the user to enter three pieces of information: name (string), age (integer), and a nested tuple containing city and country (strings).
# Logic:
# Pack these pieces of information into a single tuple.
# Unpack the tuple back into individual variables.
# Display the unpacked variables, including the elements of the nested tuple.
# Output:
# Display the packed tuple and the unpacked values.


# name = input("Enter your name: ")
# age = input("Enter your age: ")
# city = input("Enter your city: ")
# country = input("Enter your country: ")
#
# combined_loc = (city, country)
#
# info = (name, age, combined_loc)
# print(info)
#
# print(f"Your name is {info[0]}")
# print(f"Your age is {info[1]}")
# print(f"You are from {info[2][0]}, {info[2][1]}")

# Assignment 13: Tuple Statistics
# Instructions:
# Perform following tasks:
# Prompt the user to enter a tuple of integers separated by commas (e.g., 5, 10, 15, 20).
# Convert the input string to a tuple of integers.
# Calculate and display:
# The sum of all elements.
# The average of the elements.
# The maximum and minimum values.
# The number of elements in the tuple.
# Output:
# Display results of the above operations in a clear format.

# str1 = input("Enter the elements of the tuple: ")
#
# tup = tuple(int(x) for x in str1.split(sep=' '))
#
# tup = tuple(sorted(tup))
# print(tup)
#
# threshold = int(input("Enter Threshold Value: "))
# new_tup = tuple(x for x in tup if x > threshold)
# print(new_tup)

# Assignment 14: Tuple Sorting and Filtering
# Instructions:
# Perform the following tasks:
# Prompt the user to enter a tuple of integers separated by commas (e.g., 8, 3, 7, 1, 4).
# Convert the input string to a tuple of integers.
# Sort the tuple in ascending order.
# Filter out all elements greater than a specified threshold (prompt the user for this threshold).
# Display the sorted tuple and the filtered elements.
# Output:
# Display results of the above operations in a clear format.

# str1 = input("Enter the elements of the tuple: ")
#
# tup = tuple(int(x) for x in str1.split(sep=' '))
#
# tup = tuple(sorted(tup))
# print(tup)
#
# threshold = int(input("Enter Threshold Value: "))
# new_tup = tuple(x for x in tup if x > threshold)
# print(new_tup)

# Assignment 15: Create a program that stores and analyses student’s grades using dictionaries.
# Input:
# Prompt the user to enter student names and their corresponding grades.
# Store the data in a dictionary where keys are student names and values are lists of grades.
# Logic:
# Implement functions to:
# Calculate the average grade for each student.
# Find the student with the highest average grade.
# Display students who have grades above a certain threshold.
# Output:
# Display each student's average grade.
# Display the student with the highest average grade.
# Display the list of students with grades above a user-specified threshold.

# def calculate_averages(grades_dict):
#     averages = {}
#     for student, grades in grades_dict.items():
#         averages[student] = sum(grades) / len(grades) if grades else 0
#     return averages
#
# def highest_average(averages):
#     return max(averages, key=averages.get)
#
# def students_above_threshold(averages, threshold):
#     return [student for student, avg in averages.items() if avg > threshold]
#
# def main():
#     student_grades = {}
#
#     while True:
#         name = input("Enter student name (or 'done' to finish): ").strip()
#         if name.lower() == 'done':
#             break
#
#         grades = input(f"Enter grades for {name} (comma separated): ").strip()
#         grades = [float(grade) for grade in grades.split(",") if grade.strip().isdigit()]
#
#         student_grades[name] = grades
#
#     averages = calculate_averages(student_grades)
#
#     print("\nAverage Grades:")
#     for student, avg in averages.items():
#         print(f"{student}: {avg:.2f}")
#
#     # Output: Display the student with the highest average grade
#     top_student = highest_average(averages)
#     print(f"\nStudent with the highest average grade: {top_student} ({averages[top_student]:.2f})")
#
#     # Output: Display the list of students with grades above a threshold
#     threshold = float(input("\nEnter a grade threshold: "))
#     above_threshold = students_above_threshold(averages, threshold)
#
#     if above_threshold:
#         print("\nStudents with grades above the threshold:")
#         for student in above_threshold:
#             print(f"{student}: {averages[student]:.2f}")
#     else:
#         print("\nNo students with grades above the threshold.")
#
# if __name__ == "__main__":
#     main()

# Assignment 16: Develop a program to manage an inventory system for a small store.
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

# Assignment 17: Create a country capitals quiz program using dictionaries.
# Input:
# Store a dictionary of countries and their capitals.
# Ask the user to match countries with their capitals.
# Logic:
# Implement a function to shuffle the questions and keep track of correct and incorrect answers.
# Allow the user to take the quiz and provide feedback after each question.
# Calculate the final score.
# Output:
# Display the correct answer when the user gets it wrong.
# Show the final score and a summary of correct and incorrect answers.

# Assignment 18: Build a simple phonebook application using dictionaries.
# Input:
# Allow the user to add, search, update, and delete contacts in the phonebook.
# Each contact should have a name, phone number, and email.
# Logic:
# Use a dictionary where keys are contact names and values are another dictionary containing the phone number and email.
# Implement functions for adding, searching, updating, and deleting contacts.
# Ensure the phonebook is case-insensitive when searching for contacts.
# Output:
# Display all contacts after each operation.
# Display a message if a contact is not found during a search or delete operation.

# Assignment 19: Write a program that counts the frequency of each element in a list and stores the results in a dictionary.
# Input:
# Prompt the user to enter a list of elements (numbers, strings, etc.).
# Logic:
# Use a loop to count the occurrences of each element in the list.
# Store the element and its frequency as key-value pairs in a dictionary.
# Output:
# Display the dictionary with the frequency of each element.

# string = input("Enter number: ").replace(" ", "")
# ls = list(x for x in string)
# dic = {x:ls.count(x) for x in set(ls)}
# print(dic)

# Assignment 20: Create a program to manage a book collection using dictionaries.
# Input:
# Allow the user to add, remove, and search for books in the collection.
# Each book should have a title, author, genre, and year of publication.
# Logic:
# Use a dictionary where keys are book titles and values are another dictionary containing the author, genre, and year.
# Implement functions to:
# Add a new book to the collection.
# Remove a book from the collection by title.
# Search for books by genre or author.
# Display all books in the collection.
# Output:
# Display the details of all books in the collection after each operation.
# Display search results for books by genre or author.

