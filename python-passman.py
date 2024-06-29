import hashlib  # Used for hashing passwords securely
import getpass  # Used to prompt for password input without echoing

# Initialize an empty dictionary to store username-hashed password pairs
password_manager = {}


def create_account():
    """
    Prompts the user to create a new account with a username and password.
    Hashes the password for secure storage.
    """

    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password (characters won't be shown): ")

    # Hash the password using a secure algorithm (SHA-256 in this case)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Add the username-hashed password pair to the password manager dictionary
    password_manager[username] = hashed_password

    print("Account created successfully!")


def login():
    """
    Prompts the user for their username and password.
    Compares the entered password (hashed) against the stored hashed password.
    Provides feedback on login success or failure.
    """

    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password (characters won't be shown): ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username exists and the password matches (hashed comparison)
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


def main():
    """
    Provides a menu-driven interface for the password manager.
    Allows users to create accounts, login, or exit.
    """

    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break  # Exit the loop
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")


if __name__ == "__main__":
    main()