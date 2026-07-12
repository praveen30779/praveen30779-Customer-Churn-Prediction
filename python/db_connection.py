import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        if connection.is_connected():
            print("✅ MySQL Connected Successfully")

        return connection

    except Exception as e:
        print("Connection Error:", e)

if __name__ == "__main__":
    conn = get_connection()

    if conn:
        conn.close()
        print("Connection closed.")