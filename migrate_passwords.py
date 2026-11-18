import mysql.connector

from database import connect_db
from password_security import hash_password, is_hashed_password


def main():
    db = connect_db()
    cursor = None
    try:
        cursor = db.cursor()
        cursor.execute(
            "ALTER TABLE users MODIFY password VARCHAR(255) NOT NULL"
        )
        cursor.execute("SELECT id, password FROM users")
        users = cursor.fetchall()
        updates = [
            (hash_password(password), user_id)
            for user_id, password in users
            if not is_hashed_password(password)
        ]
        if updates:
            cursor.executemany(
                "UPDATE users SET password = %s WHERE id = %s",
                updates,
            )
        db.commit()
        print(f"Password aman diperbarui untuk {len(updates)} akun.")
    except mysql.connector.Error:
        db.rollback()
        raise
    finally:
        if cursor is not None:
            cursor.close()
        db.close()


if __name__ == "__main__":
    main()
