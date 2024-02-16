from typing import Self
from zk import ZK, const
from attendence import Attendance
import json  # Import the json module
from attendence import Attendance  # Import the Attendance class from your module

# Connect to the ZKTeco device
attendance_system = Attendance(ip='your_device_ip', port=4370, timeout=5)

# Define your SQL insert query with the actual table name and columns    
def get_INSERT_ON_DUPLICATE_KEY_UPDATE(): 
               insert_query = "INSERT INTO hrkit (name, privilege, password, group_id, user_id) \
               VALUES (%s, %s, %s, %s, %s) \
               ON DUPLICATE KEY UPDATE \
               name = VALUES(name), privilege = VALUES(privilege), password = VALUES(password), group_id = VALUES(group_id), user_id = VALUES(user_id)"

# Define your SQL insert query with the actual table name and columns
def get_INSERT_IGNORE():
                           
               insert_query = "INSERT IGNORE INTO hrkit (name, privilege, password, group_id, user_id) \
                  VALUES (%s, %s, %s, %s, %s)"

