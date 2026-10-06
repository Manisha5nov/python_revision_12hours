# Extract the middle characters.
string = input("Enter a string: ")
# Calculate the middle index
middle_index = len(string) // 2
# Extract the middle character(s)
if len(string) % 2 == 0:
    middle_characters = string[middle_index - 1:middle_index + 1]
else:
    middle_characters = string[middle_index]
print("Middle character(s):", middle_characters)
