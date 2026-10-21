# Print every second character.
string = input("Enter a string: ")
for i in range(0, len(string), 2):
    print(string[i], end="")
