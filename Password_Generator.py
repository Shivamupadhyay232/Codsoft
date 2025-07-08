import random
import string

def generate_password():
    print("Welcome to the Password Generator!")

    # Ask user for desired password length
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Length should be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    # Define possible characters: letters, digits, symbols
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the generated password
    print(f"\nGenerated Password: {password}")

# Run the password generator
generate_password()
