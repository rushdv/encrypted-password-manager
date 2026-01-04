import os

def set_master_password():
    master = input("Set master password: ")
    with open("master.txt", "w") as file:
        file.write(master)
    print("Master password set successfully !")

def check_master_password():
    entered = input("Enter master password: ")
    with open("master.txt", "r") as file:
        saved = file.read()
    return entered == saved

def add_password():
    site = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    with open("vault.txt", "a") as file:
        file.write(f"{site} | {username} | {password}\n")

    print("Password saved !")


def view_password():
    try:
        with open("vault.txt", "r") as file:
            print("\n===== SAVED PASSWORD =====")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No password saved yet.")


if not os.path.exists("master.txt"):
    set_master_password()


while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add new password")
    print("2. View saved password")
    print("3. Exit")

    choice = input("Choice option: ")

    if choice == "3":
        print("Exitting Password Manager....")
        break
    

    if not check_master_password():
        print("Wrong master password !")
        continue

    if choice == "1":
        add_password()
    elif choice == "2":
        view_password()
    else:
        print("Invalid choice")
    