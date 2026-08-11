# escape sequences in python
# Escape sequences are special characters in Python that are used to represent certain characters that cannot be easily typed or displayed in a string. They are preceded by a backslash (\) and have specific meanings. Here are some common escape sequences in Python:
# 1. \n - Newline: Moves the cursor to the next line. 
# 2. \t - Tab: Inserts a tab character.
# 3. \\ - Backslash: Inserts a backslash character.
# 4. \' - Single Quote: Inserts a single quote character.
# 5. \" - Double Quote: Inserts a double quote character.
# 6. \r - Carriage Return: Moves the cursor to the beginning of the line.
# 7. \b - Backspace: Moves the cursor one position back.
# 8. \f - Form Feed: Moves the cursor to the next page (not commonly used).
# 9. \v - Vertical Tab: Moves the cursor down to the next vertical tab stop.
# 10. \ooo - Octal value: Represents a character based on its octal value.
# 11. \xhh - Hexadecimal value: Represents a character based on its hexadecimal value.
# 12. \N{name} - Unicode character: Represents a Unicode character by its name.

# Example usage of escape sequences in Python:


# Using escape sequences in a string
print("Hello\nWorld")  # Output: Hello (newline) World
print("This is a tab:\tTab")  # Output: This is a tab:    Tab
print("This is a backslash: \\")  # Output: This is a backslash: \
print("Single quote: \' and Double quote: \"")  # Output: Single quote: ' and Double quote: "
print("Carriage return:\rStart")  # Output: Start (overwrites the line)
print("Backspace: ABC\bD")  # Output: ABD (B is removed)    
print("Form feed:\fNext page")  # Output: Form feed: (moves to next page)
print("Vertical tab:\vNext line")  # Output: Vertical tab: (moves down to next vertical tab stop)
print("Octal value: \101")  # Output: Octal value: A (represents the character 'A' in octal)
print("Hexadecimal value: \x41")  # Output: Hexadecimal value: A (represents the character 'A' in hexadecimal)      
