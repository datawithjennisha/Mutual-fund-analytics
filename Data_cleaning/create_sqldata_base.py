import sqlite3

# ==============================
# Connect to SQLite Database
# ==============================
try:
    conn = sqlite3.connect("bluestock_mf.db")
    cursor = conn.cursor()

    print("Connected to SQLite Database.")

    # ==============================
    # Read SQL Schema File
    # ==============================
    with open("SQL/schema.sql", "r") as file:
        schema = file.read()

    # ==============================
    # Execute SQL Script
    # ==============================
    cursor.executescript(schema)

    # ==============================
    # Save Changes
    # ==============================
    conn.commit()

    print("Tables created successfully!")

    # ==============================
    # Display Created Tables
    # ==============================
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table';
    """)

    tables = cursor.fetchall()

    print("\n========== Tables Created ==========")

    for table in tables:
        print(table[0])

except sqlite3.Error as e:
    print("SQLite Error:", e)

except FileNotFoundError:
    print(" schema.sql file not found.")
    print("Make sure it exists inside the SQL folder.")

finally:
    if 'conn' in locals():
        conn.close()
        print("\n Database connection closed.")