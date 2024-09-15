# Assignment 1: Create a decorator with arguments to print name of the
# function being executed.

# def simple_logger(func):
#     # Wrapper function that adds logging behaviour
#     def wrapper(*args, **kwargs):
#         print("Starting ", func.__name__)
#         result = func(*args, **kwargs)
#         print(f"Finished ", func.__name__)
#         return result
#     return wrapper
#
# # using the decorator without arguments
# @simple_logger
# def greet(name):
#     print(f"Hello {name}")
#
# # call the decorated function
# greet("Abhishek")

# Assignment 2: Write  Decorator to calculate Execution Time
# Tasks :
# Decorator 1: @log_func_name – prints calling function name
# Decorator 2: @log_execution_time – prints the time required for a function to execute.

# import logging
#
# # Outer function that takes the decorator arguments
# def log_to_file(log_file, log_level=logging.INFO):
#     # Configure the logging settings
#     logging.basicConfig(
#         filename=log_file,
#         level=log_level,
#         format='%(asctime)s - %(levelname)s - %(message)s'
#     )
#
# # decorator function that takes the function to be decorated
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print("Starting ", func.__name__)
#             result = func(*args, **kwargs)
#             print(f"Finished ", func.__name__)
#             return result
#
#         return wrapper
#     return decorator
#
#
# @log_to_file(log_file="atharva_log_log", log_level=logging.DEBUG)
# def greet(name):
#     print(f"Hello {name}")
#
#
# greet("Alice")

# Assignment 3: Create a basic config logger

# import time
#
#
# def log_execution_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # Record the start time
#         result = func(*args, **kwargs)  # Call the decorated function
#         end_time = time.time()  # Record the end time
#         execution_time = end_time - start_time  # Calculate the execution time
#         print(f"Function took {execution_time:.4f} seconds to execute.")
#         return result  # Return the result of the function
#     return wrapper
#
#
# def log_func_name(func):
#     # Wrapper function that adds logging behaviour
#     def wrapper(*args, **kwargs):
#         # print("Starting ", func.__name__)
#         result = func(*args, **kwargs)
#         # print(f"Finished ", func.__name__)
#         print("Name of the function is", func.__name__)
#         return result
#     return wrapper
#
#
# @log_execution_time
# @log_func_name
# def example_function():
#     # time.sleep(x)
#     for i in range(1, 10000):
#         i += 1
#     # return f"Slept for {x} seconds"
#
#
# # Calling the decorated function
# example_function()

# Assignment 4: Create an advanced config logger

# import logging
#
# logging.basicConfig(filename='basicConfig.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# # logging.debug("This is a debug message")
# # logging.info("This is an info message")
# # logging.warning("This is an error message")
# # logging.critical("This is a critical message")
#
#
# # Set up the logger
# # logging.basicConfig(filename='debug.log', level=logging.DEBUG,
# #                     format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger()
#
#
# def log_debug(func):
#     def wrapper(*args, **kwargs):
#         logger.debug(f"Function {func.__name__} begun")
#         result = func(*args, **kwargs)
#         logger.debug(f"Function {func.__name__} ended")
#
#         return result
#     return wrapper
#
#
# # Example usage:
#
#
# @log_debug
# def add_function(x, y):
#     return x + y
#
#
# @log_debug
# def detail_function(name, age):
#     return f"{name} is {age} years old."
#
#
# # Calling the decorated functions
# add_function(5, 7)
# detail_function("Alice", 30)

# Assignment 5: Use decorator to log debug messages to a log file using logging module.
# Decorator
# name: @log_execution
# Use basicConfig to configure logger
# Message to print before function executes: funcName has begun
# Message to print after function executes: funcName has ended

# import re
#
# # Read the entire file content
# with open('file.text', 'r') as file:
#     content = file.read()
#
# # Define regex pattern to match lines between 'start' and 'end'
# pattern = re.compile(r'Start(.*)End')
#
# # Find all matches
# matches = pattern.findall(content)
#
# # Print the matches
# for match in matches:
#     print(match.strip())

# Assignment 6: Use decorator to log debug messages to a log file using logging module.
# Decorator
# name: @log_execution
# Use basicConfig to configure logger
# Message to print before function executes: funcName has begun
# Message to print after function executes: funcName has ended
# Challenge: If an exception is encountered in the function, (zeroDivisionError), handle the exception in the decorator, such that exception gets logged into a separate log file.
# 2 separate loggers need to be defined here.
# Try catch around the func call in except condition call the other logger.in try block call the debug logger

# import re
# str = ['Apple pie is delicious',
#       'Under the bed, there is a cat',
#       'Notes from the meeting!',
#       '1234a5678b9aaa',
#       'Do not forgot to check the details!']
#
# # print(str)
#
# print(re.findall(r'\b[aeiouAEIOU]\w*[bcdfghjklmnpqrstvwxyzBCDFGHKLMNPQRSTVWXYZ]\b', "Apple pie is delicious"))
# print(re.findall(r'[\d]+[^\d]', "Abc23424gan34ababc456"))
# print(re.findall(r'Note(.*)!', "Note atharva !"))


# Assignment 8: Read a file and perform following operations on it:
# Task 1: Find and print all words that start with a vowel (a, e, i, o, u) and end with a consonant (b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z).
# Task 2: Extract and print all sequences of digits that are followed by a non-digit character.
# Task 3: Identify and print all lines that start with the word "Note" and end with an exclamation mark (!).
# Contents of file:
# Here are some examples:
# 1. Apple pie is delicious.
# 2. Under the bed, there is a cat!
# 3. Notes from the meeting!
# 4. 1234a5678b9aaa
# 5. Do not forget to check the details!

