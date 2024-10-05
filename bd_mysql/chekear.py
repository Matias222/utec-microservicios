import mysql.connector
from mysql.connector import Error

def connect_and_query():
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            database='gestionpedidos',
            user='myuser',  # Replace with your MySQL username
            password='mypassword'  # Replace with your MySQL password
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            # Create a cursor object
            cursor = connection.cursor()

            # Execute the query
            cursor.execute("SELECT * FROM pedidos")

            # Fetch all rows from the executed query
            rows = cursor.fetchall()

            # Print the results
            print("Fetching all rows from pedidos table:")
            for row in rows:
                print(row)

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    connect_and_query()
