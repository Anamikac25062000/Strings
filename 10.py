# count() built-in string

input_value = input("Enter a string: ")
substring = input("Enter the substring to find: ")

try:
    index = input_value.index(substring)
    print(f"Original string: '{input_value}'")
    print(f"Index of '{substring}': {index}")
except ValueError:
    print(f"'{substring}' not found in the string.")
