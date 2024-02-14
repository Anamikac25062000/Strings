# isdigit() built-in string

input_value = input("Enter a string: ")
if input_value.isdigit():
    print(f"The string '{input_value}' consists only of digits.")
else:
    print(f"The string '{input_value}' contains non-digit characters.")
