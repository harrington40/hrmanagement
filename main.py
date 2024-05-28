from zk import ZK, const
import threading
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from attendence import Attendance  # Assumed file name change from 'attendence' to 'attendance' for consistency
from users import Enrollment
from threading import Thread
import os

from utility import read_from_db, write_to_db, update_db

load_dotenv()  # This loads the variables from .env

#
class AttendanceManager:
    def __init__(self, attendance_system):
        self.attendance_system = attendance_system

    def store_attendance_data(self):
        """Fetches and stores attendance records in the 'attendance' database table."""
        if not self.attendance_system.conn:
            if not self.attendance_system.connect():
                print("Failed to connect to the device.")
                return

        try:
            attendance_records = self.attendance_system.get_attendance()
            print("Attendance Records: ", attendance_records)

            if attendance_records:
                for record in attendance_records:
                    user_id = record['User ID']
                    timestamp = record['Timestamp']
                    status = record['Status']

                    # Check if user_id is a digit (thus numeric)
                    if not user_id.isdigit():
                        print(f"Skipping record with non-numeric User ID: {user_id}")
                        continue

                    # Prepare data for insertion
                    data = (user_id, timestamp, status)
                    print("Data to insert: ", data)

                    # Define SQL insert query, adjust column names as per your database schema
                    insert_query = """
                    INSERT INTO Attendance (employeeId, timeStamp, status)
                    VALUES (%s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                    timeStamp=VALUES(timeStamp), status=VALUES(status)
                    """

                    # Insert the record into the database
                    write_to_db(insert_query, data)

                print("Attendance records have been stored in the database 2024.")
            else:
                print("No attendance records to process.")
        except Exception as e:
            print(f"Error fetching or storing attendance data: {e}")

# Usage example
if __name__ == "__main__":
    attendance_system = Attendance('192.168.0.201', port=4370)
    attendance_manager = AttendanceManager(attendance_system)
    attendance_manager.store_attendance_data()

