# isalnum() built-in string

input_value = input("Enter a string: ")
if input_value.isalnum():
    print(f"The string '{input_value}' consists only of alphanumeric characters.")
else:
    print(f"The string '{input_value}' contains non-alphanumeric characters.")
