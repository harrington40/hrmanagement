from zk import ZK, const
import threading
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import data
import os

# Create an instance of the Facade
from attendence import Attendance
from utility import read_from_db, update_db, write_to_db

"""
This script demonstrates the use of the AttendanceFacade class to record attendance.
The AttendanceFacade class provides a simplified interface to the attendance recording system,
hiding the underlying complexity of the attendance management operations.

Usage:
    This script creates an instance of AttendanceFacade and uses it to record an attendance
    entry with specified user details.
"""
load_dotenv()  # This loads the variables from .env
# Define your SQL insert query with the actual table name and columns
attendance_system = Attendance('192.168.0.201', port=4370)
  # Get all users from the ZKTeco device
all_users = attendance_system.get_all_users()
if all_users:
        for user in all_users:
            # Create user_data dictionary for each user
            user_data = {
                'uid': user['uid'],
                'name': user['name'],
                'privilege': 1 if user['privilege'] == 'Admin' else 0,
                'password': user['password'],
                'group_id': user['group_id'],
                'user_id': user['user_id']
            }

        insert_query = "INSERT INTO ClockInOut ( uid, name, privilege, password, group_id, user_id) \
                    VALUES (%s, %s, %s, %s, %s, %s)"
        # Define your SQL insert query with the actual table name and columns
        insert_query = "INSERT IGNORE INTO ClockInOut (uid, name, privilege, password, group_id, user_id) \
               VALUES (%s, %s, %s, %s, %s)"


        # Create a tuple with the values extracted from the user_data dictionary
        data = (user_data['uid'], user_data['name'], user_data['privilege'],
            user_data['password'], user_data['group_id'], user_data['user_id'])

        # Create the write_thread with the insert_query and data
        write_thread = threading.Thread(target=write_to_db, args=(insert_query, data))

user_timeStamp = attendance_system.get_attendance(user_id = None)
if user_timeStamp:
        for time in user_timeStamp:
                # Create user_data dictionary for each user
            time_data = {
                'user Id': time['user Id'],
                'timestamp': time['timestamp'],
                'status': time['status']
            }






        # Example usage
        write_thread = threading.Thread(target=write_to_db, args=("YOUR_INSERT_QUERY", data))
        read_thread = threading.Thread(target=read_from_db, args=("YOUR_SELECT_QUERY",))
        update_thread = threading.Thread(target=update_db, args=("YOUR_UPDATE_QUERY", data))

        write_thread.start()
        read_thread.start()
        update_thread.start()

        write_thread.join()
        read_thread.join()
        update_thread.join()
