from db_connection import get_connection

connection = get_connection()

if connection:
    print("Database Connected Successfully")
    connection.close()