# Write a Python code to remove all characters except a            
# Sample String : 'exercises' 
# Expected Result : 'eee' (Removed all characters except special character : e) 


input_value = input("Enter a string: ")
character = input("Enter the character: ")

result = ''.join(char for char in input_value if char == character)
print(result)


