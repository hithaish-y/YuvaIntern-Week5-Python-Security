import sqlite3

DB_NAME = "users.db"

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL
    )""")
    conn.commit()
    conn.close()

def add_user(username, password, email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = f"INSERT INTO users (username, password, email) VALUES ('{username}', '{password}', '{email}')"
    cursor.execute(query)
    conn.commit()
    conn.close()

def find_user(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = f"SELECT id, username, email FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def main():
    setup_database()
    print("User Management Application")
    print("1. Add user")
    print("2. Find user")
    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        email = input("Email: ")
        try:
            add_user(username, password, email)
            print("User added successfully.")
        except Exception as error:
            print("Database error:", error)
    elif choice == "2":
        username = input("Username: ")
        try:
            print("Users:", find_user(username))
        except Exception as error:
            print("Database error:", error)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
