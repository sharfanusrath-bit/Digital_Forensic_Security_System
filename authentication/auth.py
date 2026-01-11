import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    print("\n--- User Registration ---")

    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (admin/investigator): ")
    ai_choice = input("Enable AI authentication? (yes/no): ")

    ai_enabled = 1 if ai_choice.lower() == "yes" else 0
    hashed_password = hash_password(password)

    try:
        conn = sqlite3.connect("database/users.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, password, role, ai_enabled) VALUES (?, ?, ?, ?)",
            (username, hashed_password, role, ai_enabled)
        )

        conn.commit()
        conn.close()
        print("User registered successfully!")

    except sqlite3.IntegrityError:
        print("Username already exists. Try another.")

def login_user():
    print("\n--- User Login ---")

    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hash_password(password)

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT role, ai_enabled FROM users WHERE username=? AND password=?",
        (username, hashed_password)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        role, ai_enabled = result
        print("Login successful!")
        print("Role:", role)

        if ai_enabled == 1:
            print("AI authentication enabled (will be added next)")
        else:
            print("AI authentication not enabled")

        return True
    else:
        print("Invalid username or password")
        return False
