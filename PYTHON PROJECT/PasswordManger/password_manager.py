from cryptography.fernet import Fernet, InvalidToken  # Correctly import InvalidToken

# Function to write the encryption key to a file (run once to generate the key)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key from a file
def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

# Get the master password from the user
master_pwd = input("What is the master password? ")
key = load_key()
fer = Fernet(key)

# Function to view passwords
def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.strip()
                if "|" in data:
                    user, encrypted_pass = data.split("|")
                    try:
                        # Attempt to decrypt the password
                        decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
                        print(f"User: {user} | Password: {decrypted_pass}")
                    except InvalidToken:
                        print(f"Error: Unable to decrypt the password for {user}. It may have been encrypted with a different key.")
                else:
                    print("Malformed line, skipping.")
    except FileNotFoundError:
        print("No passwords found. Add some first!")

# Function to add passwords
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd + "\n")
    print(f"Password for {name} added.")

# Main loop to manage the user's choice
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please choose 'view' or 'add'.")
