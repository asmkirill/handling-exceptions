from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:

    # Removes whitespace from input string
    str_with_ints_clear = str_with_ints.replace(' ', '')

    list_num = []
    list_str = []

    # Separate digits and non-digits into two lists
    for i in str_with_ints_clear:
        try:
            list_num.append(int(i))
        except:
            list_str.append(i)

    list_str_len = len(list_str)
    list_num_len = len(list_num)

    if list_str == []:
        # If there are no non-digits, perform division
        try:
            return list_num[0] / list_num[1]

            # Check for zero division
            if list_num[1] == 0:
                raise ZeroDivisionError
        except ZeroDivisionError as zde:
            return f"Error code: {zde}"

    elif list_num_len == 1 and list_str_len == 1:
        # If there is only one digit and one non-digit, perform division
        try:
            list_num[0] / int(list_str[0])
            # Check for non-integer non-digit
            if isinstance(list_str[0], str):
                raise ValueError
        except ValueError as ve:
            return f"Error code: {ve}"

    else:
        # Otherwise, assume two non-digits and perform division
        try:
            int(list_str[0]) / int(list_str[1])
            # Check for non-integer non-digits
            if isinstance(list_str[0], str) or isinstance(list_str[1], str):
                raise ValueError
        except ValueError as ve:
            return f"Error code: {ve}"

        
"""
    Code is using built-in Python exceptions to handle division by zero and invalid literal errors.
    Error messages will be printed automatically by Python's error handling system 
    and that there is no need to print them manually in the code.
"""


