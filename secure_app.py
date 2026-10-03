import sqlite3
import hashlib
import re
import secrets
import hmac
import getpass

DB_NAME = "users_secure.db"

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )""")
    conn.commit()
    conn.close()

def validate_username(username):
    return bool(re.fullmatch(r"[A-Za-z0-9_]{3,30}", username))

def validate_email(email):
    return bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email))

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), bytes.fromhex(salt), 100_000
    ).hex()
    return password_hash, salt

def add_user(username, password, email):
    if not validate_username(username):
        raise ValueError("Invalid username format.")
    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")
    if not validate_email(email):
        raise ValueError("Invalid email format.")

    password_hash, salt = hash_password(password)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password_hash, salt, email) VALUES (?, ?, ?, ?)",
        (username, password_hash, salt, email)
    )
    conn.commit()
    conn.close()

def find_user(username):
    if not validate_username(username):
        return []
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username, email FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchall()
    conn.close()
    return result

def main():
    setup_database()
    print("Secure User Management Application")
    print("1. Add user")
    print("2. Find user")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        username = input("Username: ").strip()
        password = getpass.getpass("Password: ")
        email = input("Email: ").strip()
        try:
            add_user(username, password, email)
            print("User added successfully.")
        except ValueError as error:
            print(error)
        except sqlite3.IntegrityError:
            print("Username or email already exists.")
        except sqlite3.Error:
            print("Unable to complete the database operation.")
    elif choice == "2":
        username = input("Username: ").strip()
        try:
            users = find_user(username)
            print("Users:", users) if users else print("No user found.")
        except sqlite3.Error:
            print("Unable to complete the database operation.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
