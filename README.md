
# Simple Password Manager (Educational Purposes Only)

This Python script provides a basic password manager for educational purposes. It allows users to create accounts with usernames and passwords, securely stores hashed passwords, and enables login functionality.

## Important Note:

**This script is for demonstration only and should not be used in a production environment. It lacks critical security features for real-world password management.** ⚠️

## How to Use (macOS commands)

1. **Clone this repository to your local machine** (use that fancy git magic 🪄).
2. **Create a virtual environment on your vscode python `-m venv env`**
3. **Activate the virtual environment `source venv/bin/activate`**
4. **Install the required libraries**: `hashlib` and `getpass` are included in the standard Python library (no extra downloads needed ✅).
5. **Run the script** using `python password_manager.py` (like a coding wizard 🧙‍♂️).
6. **Follow the on-screen prompts** to create an account or login (easy-peasy 🥳).

## What it Does

The script offers the following options, making password management a breeze:

- **Create Account**: Enter a desired username and password. The password will be securely hashed using SHA-256 (for educational purposes) before storage (think of it like scrambling your password with a secret code 🔑).
- **Login**: Enter your username and password. The entered password is hashed and compared against the stored hashed password for authentication (like a secret handshake 🤝).

## Taking a Peek Inside

The script is organized into three main functions, like well-oiled gears working together ⚙️:

- `create_account()`: Prompts the user for a username and password, hashes the password, and stores the username-hashed password pair in a dictionary (think of it like a secure address book for your usernames and scrambled passwords 📒).
- `login()`: Prompts the user for login credentials, hashes the entered password, and verifies it against the stored hashed password for the provided username (like checking a secret key to unlock a door 🔐).
- `main()`: Provides a menu-driven interface for the password manager, allowing users to create accounts, login, or exit (like a control center for your password needs 🕹️).
- 
 ### `if __name__ == "__main__":` - What Does It Do?

The line `if __name__ == "__main__":` is a common construct in Python scripts. It is used to determine whether the script is being run as the main program or if it is being imported into another script as a module.

#### `__name__` Variable
- `__name__` is a special built-in variable in Python.
- When a Python script is run directly, `__name__` is set to `"__main__"`.
- When the script is imported as a module in another script, `__name__` is set to the name of the script/module.

#### The Condition
- `if __name__ == "__main__":` checks whether the script is being run directly.
- If the script is being run directly, the condition evaluates to `True`.
- If the script is imported as a module, the condition evaluates to `False`.

#### The `main()` Function
- `main()` is typically defined as the main entry point for the script.
- Placing `main()` within this `if` block ensures that `main()` is only executed when the script is run directly, not when it is imported as a module.


## We've Got Your Back (with Comments)

The code is well-commented to explain the purpose of each function and code block, making it easy to understand even for coding newbies 👶. We've also added improvements:

- **Descriptive variable names**: We've used clear and descriptive names for variables, making the code more readable (like using labels in a notebook 🏷️).
- **Docstrings**: We've added comments at the beginning of functions to explain their purpose in more detail (like little instruction manuals for each function 📖).

## Security in Mind (But More Can Be Done)

While we've explained the limitations of SHA-256, for real-world use, consider implementing more robust password hashing algorithms like `bcrypt` or `Argon2` (think of it as using extra strong encryption 🛡️). Key derivation functions (KDFs) can further improve password security (like adding an extra layer of protection 🧅).

## Room for Growth

- **Error Handling**: We can make the script more robust by handling invalid input, password manager file operations, and other potential errors (like catching bugs before they cause problems 🐛).
- **Persistence**: This script doesn't persist the password manager data. We can explore options like database storage or encrypted files for a more permanent solution (like storing your passwords in a secure vault 🏦).

## Remember...

This code is provided for educational purposes only. It should not be used in a production environment without significant security improvements (don't use this for your bank account just yet! 🏦).

---

Feel free to contribute to this project by submitting issues or pull requests. Happy coding! 🧙‍♂️
