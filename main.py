from zk import ZK, const
import threading
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from attendence import Attendance
from users import Enrollment
import os

# Assuming 'attendence.py' and 'utility.py' are correctly implemented

from utility import read_from_db, write_to_db, update_db

load_dotenv()  # This loads the variables from .env

# Initialize the Attendance system
attendance_system = Attendance('192.168.0.201', port=4370)

def insert_user_data():
    all_users = attendance_system.get_all_users()
    print("WWWWW", all_users)
    if all_users:
        for user in all_users:
            user_data = {
                'uid': user['uid'],
                'name': user['name'],
                'privilege': 1 if user['privilege'] == 'Admin' else 0,
                'password': user['password'],
                'group_id': user['group_id'],
                'user_id': user['user_id']
            }
            insert_query = "INSERT IGNORE INTO ClockInOut (uid, name, privilege, password, group_id, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
            data_tuple = (user_data['uid'], user_data['name'], user_data['privilege'], user_data['password'], user_data['group_id'], user_data['user_id'])
            write_to_db(insert_query, data_tuple)

def get_attendance_data():
    user_timeStamp = attendance_system.get_attendance(user_id=None)
    print("DDDD",user_timeStamp)
    try:
        if user_timeStamp:
            for time in user_timeStamp:
                time = {
                
                'Status': time['Status'],
                'TimeStamp': time['TimeStamp'],
                'User ID': time['User ID'],
                'ClockoutRule': time['clockoutRule']
                }
            # Create the insert query using the data
                data_tuple = ( time['User ID'], time['TimeStamp'], time['Status'], time['clockoutRule'])
                insert_query = "INSERT IGNORE INTO AttendanceCalculations (clockinRule, clockoutRule, noClockin, noClockout, asLate, earlyLeave, createdAt, updatedAt, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE status=time['Status'], timeStamp=time['TimeStamp']"
           
            # Insert the attendance data into the database
                write_to_db(insert_query, data_tuple)
            print("Attendance records have been stored in the database.")
    except Exception as e:
            print(f"Error fetching or storing attendance data: {e}")


def store_attendance_data(self, user_id=None):
    """Fetches and stores attendance records in the 'attendance' database table."""
    if not self.conn:
        print("Device not connected")
        return

    try:
        # Get attendance records, formatted
        attendance_records = self.get_attendance(user_id)
        
        for record in attendance_records:
            # Prepare data for insertion
            data = (record['User ID'], record['Timestamp'], record['Status'])

            # Define SQL insert query, adjust column names as per your database schema
            insert_query = """
            INSERT INTO attendance (user_id, timestamp, status)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
                timestamp=VALUES(timestamp), status=VALUES(status)
            """

            # Insert the record into the database
            write_to_db(insert_query, data)

        print("Attendance records have been stored in the database.")
    except Exception as e:
        print(f"Error fetching or storing attendance data: {e}")



# Run database operations in separate threads
thread_list = [
     threading.Thread(target= get_attendance_data),
    threading.Thread(target=insert_user_data),
  
    # Add other database operations here if necessary
]

# Start threads
for thread in thread_list:
    thread.start()

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

