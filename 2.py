# Print even length words in a string. 
# Sample String : ''I love coding" 
# Expected Result : “love, coding” 


input_value = input("Enter a string: ")

length= [word for word in input_value.split() if len(word) % 2 == 0]
result = ", ".join(length)
print(result)
