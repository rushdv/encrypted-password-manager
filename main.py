import os
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass


# ---------- Key Management ---------- #

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) 

def load_key():
    return open("key.key", "rb").read()

# ---------- Encryption / Decryption ---------- #

def encrypt(text):
    f = Fernet(load_key())
    return f.encrypt(text.encode()).decode()

def decrypt(text):
    f = Fernet(load_key())
    return f.decrypt(text.encode()).decode()

# ---------- Master Password  ---------- #

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def set_master_password():
    master = getpass("Set master password: ")
    confirm = getpass("Confirm master password: ")

    if master != confirm:
        print("Passwords do not match. Try again.")
        return set_master_password()
    
    with open("master.txt", "w") as file:
        file.write(hash_password(master))

    print("Master password set successfully !")

def check_master_password():
    entered = getpass("Enter master password: ")
    with open("master.txt", "r") as file:
        saved = file.read()
    return hash_password(entered) == saved

# ---------- Password Vault ---------- #

def add_password():
    site = input("Website: ")
    username = input("Username: ")
    password = getpass("Password: ")

    data = f"{site}|{username}|{password}"
    encrypted_data = encrypt(data)

    with open("vault.txt", "a") as file:
        file.write(f"{encrypted_data}\n")

    print("Password saved securely!")

def view_password():
    if not os.path.exists("vault.txt"):
        print("No password saved yet.")
        return
    
    print("\n===== SAVED PASSWORDS =====")
    with open("vault.txt", "r") as file:
        for line in file:
            decrypted = decrypt(line.strip())
            site, user, pwd = decrypted.split("|")
            print(f"Website: {site}, Username: {user}, Password: {pwd}")


def search_password():
    keyword = input("Enter website to search: ").lower()

    found = False
    with open("vault.txt", "r") as file:
        for line in file:
            decrypted = decrypt(line.strip())
            if keyword in decrypted.lower():
                site, user, pwd = decrypted.split("|")
                print(f"Website: {site}, Username: {user}, Password: {pwd}")
                found = True
    
    if not found:
        print("No matching entries found.")

# ---------- Main Logic ---------- #

if not os.path.exists("key.key"):
    generate_key()

if not os.path.exists("master.txt"):
    set_master_password()

# Authentication Loop
attempts = 3
authenticated = False

while attempts > 0:
    if check_master_password():
        authenticated = True
        break
    else:
        attempts -= 1
        print(f"Wrong master password! {attempts} attempts left.")

if not authenticated:
    print("Too many failed attempts. Exiting...")
    exit()


# Main Menu Loop
while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add new password")
    print("2. View saved passwords")
    print("3. Search password")
    print("4. Exit")

    choice = input("Choice option: ")

    if choice == "4":
        print("Exiting Password Manager....")
        break 

    if choice == "1":
        add_password()
    elif choice == "2":
        view_password()
    elif choice == "3":
        search_password()
    else:
        print("Invalid choice")

