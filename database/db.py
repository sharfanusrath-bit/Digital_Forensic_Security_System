import sqlite3
import os

def create_database():
    # Create database folder if it does not exist
    if not os.path.exists("database"):
        os.makedirs("database")

    # Connect to SQLite database (this creates the file)
    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        ai_enabled INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

    print("Database and users table created successfully")

# Run this file directly
if __name__ == "__main__":
    create_database()