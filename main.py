MASTER_PASSWORD = "tanzim313"

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


while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add new password")
    print("2. View saved password")
    print("3. Exit")

    choice = input("Choice option: ")

    if choice == "3":
        print("Exitting Password Manager....")
        break
    
    master = input("Enter master password: ")

    if master != MASTER_PASSWORD:
        print("Wrong master password !")
        continue

    if choice == "1":
        add_password()
    elif choice == "2":
        view_password()
    else:
        print("Invalid choice")
    