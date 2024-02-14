# replace() built-in string

input_value = input("Enter a string: ")
old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the new substring: ")
modified_string = input_value.replace(old_substring, new_substring)

print(f"Original string: '{input_value}'")
print(f"Modified string: '{modified_string}'")
