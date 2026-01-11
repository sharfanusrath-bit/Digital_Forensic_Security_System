from authentication.auth import register_user, login_user

def start_system():
    while True:
        print("\n--- Digital Forensic Security System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    start_system()
