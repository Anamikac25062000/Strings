# find() built-in string

input_value = input("Enter a string: ")
substring = input("Enter the substring to find: ")
index = input_value.find(substring)

if index != -1:

    print(f"Original string: '{input_value}'")
    print(f"Index of '{substring}': {index}")
else:
    print(f"'{substring}' not found in the string.")
