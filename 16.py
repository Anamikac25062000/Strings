# isupper() built-in string

input_value = input("Enter a string: ")
if input_value.isupper():
    print(f"The string '{input_value}' is in lowercase.")
else:
    print(f"The string '{input_value}' is not in lowercase or contains non-alphabetic characters.")
