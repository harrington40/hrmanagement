import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()  # This loads the variables from .env
# Now you can use os.environ.get as shown previously

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get('DB_HOST'),   
            user=os.environ.get('DB_USER'),        
            password=os.environ.get('DB_PASSWORD'), 
            database='hrkit'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        return None
    

def write_to_db(query, data):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

def read_from_db(query):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results

def update_db(query, data):
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()




# Function definitions for database interactions (create_db_connection, write_to_db, etc.) remain unchanged

def format_attendance_records(attendance_records):
    """
    Formats multiple attendance records for display or further processing.

    Args:
        attendance_records (list): A list of dictionaries, each containing the keys 'user_id', 'timestamp', and 'status'.

    Returns:
        list: A list of strings, each a formatted string representation of an attendance record.
    """
    formatted_records = []
    status_meaning = {1: "Check-in", 2: "Check-out"}

    for record in attendance_records:
        # Convert the timestamp to a more readable format
        timestamp_str = record['timestamp'].strftime("%Y-%m-%d %H:%M:%S")

        # Determine the status meaning
        record_status = status_meaning.get(record['status'], "Unknown")

        # Create a formatted string with the attendance record information
        formatted_record = (f"User ID: {record['user_id']}, "
                            f"Timestamp: {timestamp_str}, "
                            f"Status: {record_status} ({record['status']})")
        formatted_records.append(formatted_record)

    return formatted_records




# Example usage of the format_attendance_record function
if __name__ == "__main__":
    # Sample record for demonstration
    attendance_records = [
    {'user_id': '1', 'timestamp': datetime(2023, 10, 19, 1, 37, 54), 'status': 1},
    {'user_id': '1', 'timestamp': datetime(2023, 10, 20, 8, 15, 30), 'status': 2}
]

    formatted_records = format_attendance_records(attendance_records)
    for record in formatted_records:
        print(record)


