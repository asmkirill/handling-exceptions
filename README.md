# Handling exceptions

This is a Python project for block that verifies user input in a specific format. 
The input consists of a string containing two integers separated by a space, with each integer coming from a different text area.

The task is to perform the division operation on the two integers (a / b) and return the result as a float, or raise a suitable built-in Python exception 
with an informative error message.

The structure of the error message should be as follows:
"Error code: {error message}".

arguments of a function - two integers, separated by spaces:
divide("8 2")
4.0

divide("6 0")
"Error code: division by zero"

divide("$ 2")
"Error code: invalid literal for int() with base 10: '$'"
