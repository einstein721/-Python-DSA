def check_character_case(char):
    """Function to determine if a character is uppercase or lowercase."""
    # Check if the character is an uppercase letter
    if char.isupper():
        return "Uppercase"
    # Check if the character is a lowercase letter
    elif char.islower():
        return "Lowercase"
    # Handle inputs that are neither (e.g., numbers, symbols)
    else:
        return "Neither uppercase nor lowercase"

# Ask the user to input a single character
user_char = input("Enter a single character: ")

# Ensure the user only inputted exactly one character before proceeding
if len(user_char) == 1:
    # Call the function and print the result
    result = check_character_case(user_char)
    print(f"The character '{user_char}' is: {result}")
else:
    print("Error: Please enter exactly one character.")
