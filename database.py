import sqlite3

# ---------------- DATABASE CONNECTION ---------------- #

conn = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ---------------- CREATE TABLE ---------------- #

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()

# ---------------- ADD USER ---------------- #

def add_user(username, password):

    try:

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        conn.commit()

        return True

    except:

        return False

# ---------------- LOGIN USER ---------------- #

def login_user(username, password):

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    data = cursor.fetchone()

    return data

# ---------------- CHECK USER ---------------- #

def user_exists(username):

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    data = cursor.fetchone()

    return data is not None