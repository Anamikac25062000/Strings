# isalpha() built-in string

input_value = input("Enter a string: ")
if input_value.isalpha():
    print(f"The string '{input_value}' consists only of alphabetic characters.")
else:
    print(f"The string '{input_value}' contains non-alphabetic characters.")
