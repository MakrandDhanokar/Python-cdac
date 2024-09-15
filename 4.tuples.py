# Assignment 1: Create a program that converts a list of tuples into a dictionary.
# Input:
# Prompt the user to enter a list of tuples, where each tuple contains two elements (key, value).
# Logic:
# Convert the list of tuples into a dictionary.
# Ensure that keys in the dictionary are unique. If there are duplicate keys, use the last occurrence.
# Output:
# Display the resulting dictionary.

size = int(input("Enter the size of the list: "))
list_of_tuple = [eval(input("Enter the tuple: ")) for _ in range(size)]
dictionary = dict(list_of_tuple)
print(f"The Dictionary = {dictionary}")

# Assignment 2: Write a program that counts the frequency of each element in a list and stores the results in a dictionary.
# Input:
# Prompt the user to enter a list of elements (numbers, strings, etc.).
# Logic:
# Use a loop to count the occurrences of each element in the list.
# Store the element and its frequency as key-value pairs in a dictionary.
# Output:
# Display the dictionary with the frequency of each element.

list1 = eval(input("Enter the list of elements: "))
dict1 = {item: list1.count(item) for item in set(list1)}
print(dict1)

# Assignment 3: Create a country capitals quiz program using dictionaries.
# Input:
# Store a dictionary of countries and their capitals.
# Ask the user to match countries with their capitals.
# Logic:
# Allow the user to take the quiz and provide feedback after each question. Ask if user wishes to play more.
# Calculate the final score.
# Output:
# Display the correct answer when the user gets it wrong.
# Show the final score vs no of attempted questions.

# import random
#
# dict = {"China": "Beijing", "India": "New Delhi", "Bangladesh": "Dhaka", "Russia": "Moscow", "Japan": "Tokyo"}
# size = len(dict)
# choice = 1
#
# while choice:
#     score = 0
#
#     for i in range(size):
#         country = random.choice(list(dict.keys()))
#         ans = input(f"What is the capital of {country}: ")
#         if ans == dict[country]:
#             score += 1
#         dict.pop(country)
#     print(f"You completed the Quiz\n Your score is {score}/ {size}")
#     choice = int(input("Do you want to play Again, Enter 1 otherwise 0: "))
#
#     if choice == 0:
#         break

# Assignment 8: Apply list comprehensions to find prime numbers.
#
# Generate a list of prime numbers between 1 and 50 using a list comprehension.
#
# Print the resulting list.

# # method 1
# limit = 50
# primes = [num for num in range(2, limit + 1)
#           if not any(num % i == 0 for i in range(2, int(num**0.5) + 1))]
#
# print(primes)
#
# # method 2
# limit = 50
# primes = [num for num in range(2, limit + 1)
#           if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
#
# print(primes)

# Assignment 4: List Comprehensions with Conditional Expressions (Use if-else conditions inside list comprehensions)
# Task:
# Create a list of numbers from 1 to 10.
# Use a list comprehension to create a new list where each number is squared if it's even, and cubed if it's odd.
# Print the resulting list.

# print([i**2 if i % 2 == 0 else i**3 for i in range(1, 11)])

# Assignment 5: Use dictionary comprehensions to count the frequency of elements in a list.
# Task:
# Given a list of words ['apple', 'banana', 'apple', 'orange', 'banana', 'apple'], use a dictionary comprehension to create a dictionary that counts the frequency of each word in the list.
# Print the resulting dictionary.

# Assignment 6: Write a program that prompts the user to enter a sentence, splits it into words, and creates a dictionary mapping each word to its length using dictionary comprehension.
# Input:
# Prompt the user to enter a sentence
# Logic:
# Split the sentence into individual words.
# Use dictionary comprehension to create a dictionary where each word is a key, and its length is the corresponding value.
# Output:
# Display the dictionary showing each word and its length.

# print({i: len(i) for i in input("Enter a Sentence: ").split()})

# Assignment 1:
# Use Strip Function to :
# Removing leading / trailing Whitespace - strip()
# Removing Specific Characters - strip(chars)
# Removing Leading Characters - lstrip(chars)
# Removing Trailing Characters - rstrip(chars)

# str1 = input("Enter a string: ")
# print(f"Removing Whitespace: {str1.strip()}")
# print(f"Removing Specific Character : {str1.strip('H')}")
# print(f"Removing Leading Character: Hi {str1.lstrip()}")
# print(f"Removing Trailing Character: {str1.rstrip()}", "Hi")

# Assignment 2:
# Use split () and Join () for :
# Splitting a String into Words – split()
# Splitting a String by a Custom Delimiter - split(delimiter)
# Joining a List into a String with a Space – “ ”.join(listname)
# Joining a List into a String with a Custom Separator
#
# Splitting and Joining a Sentenced

# li1 = "Atharva Makrand Ram Daksh".split(" ")
# li2 = "Apple-Mango-Banana-Watermelon".split("-")
# str1 = " ".join(li1)
# str2 = "-".join(li2)

# print(li1)
# print(li2)
# print(str1)
# print(str2)

# Assignment 3: Write a program that checks whether a given string is a palindrome (a string that reads the same backward as forward).
# Input:
# Prompt the user to enter a string.
# Logic:
# Remove any spaces and convert the string to lowercase.
# Check if the string reads the same forward and backward.
# Output:
# Display whether the string is a palindrome.

# str1 = input("Enter a String: ").lower()
# print("Palindrome" if str1.lower() == str1[::-1] else "Not a Palindrome")

# Assignment 4: Create a program that checks if two strings are anagrams (two strings that contain the same characters in a different order).
# Input:
# Prompt the user to enter two strings.
# Logic:
# Remove spaces and convert both strings to lowercase.
# Sort the characters in both strings and compare them.
# Output:
# Display whether the strings are anagrams.

# from collections import Counter
# print("Anagram" if sorted(input("Enter the string1: ")) == sorted(input("Enter the string2: ")) else "Not anagram")
# print("Anagram" if Counter(input("Enter the string1: ")) == Counter(input("Enter the string2: ")) else "Not anagram")

# Assignment 5:
# Use find() and replace() for:
# Find the First Occurrence of a Substring – text.find(substring)
#  Find All Occurrences of a Substring – text.find(substring)
# Replace First Occurrence of a Substring - text.replace(old, new, 1)
# Replace All Occurrences of a Substring - text.replace(old, new)

# paragraph = "quick brown fox jumps over the lazy and quick dog"
#
# print(paragraph.find("quick"))
# print(paragraph.rfind("quick"))
# print([i for i in range(len(paragraph)) if paragraph.startswith('quick', i)])
# print(paragraph.replace("brown", "black"))
# print(paragraph.replace("quick", "Quick", 1))

# Assignment 6: Replace Every Alternate Word in a Paragraph
# Input:
# A single string paragraph that represents a paragraph of text.
# Output:
# A new string where every alternate word in the input paragraph is replaced with the word 'replaced'.
# Logic :
# Use the split() method to divide the paragraph into a list of words.
# Replacing Alternate Words:
# Iterate through the list of words. Use the index of each word to determine if it is an alternate word. Replace every second word (i.e., words at odd indices) with the word 'replaced'.
# Joining Words:
# Combine the list of modified words back into a single string using the join() method, ensuring that words are separated by spaces.

# li = "quick brown fox jumps over the lazy dog".split()
# li2 = ["replaced" if i % 2 != 0 else li[i] for i in range(0, len(li))]
#
# print(" ".join(li))
# print(" ".join(li2))

