# count() built-in string

input_value = input("Enter a string: ")
substring = input("Enter the substring to count: ")
occurrences = input_value.count(substring)

print(f"Original string: '{input_value}'")
print(f"Occurrences of '{substring}': {occurrences}")
