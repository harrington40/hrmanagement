import json
import re
from zk import ZK, const
from utility import write_to_db, format_attendance_records
from base import ZKBase
from utility import format_attendance_records
class Enrollment:
    def __init__(self, ip, port=4370, timeout=5):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.conn = None

    def connect(self):
        try:
            self.conn = ZK(self.ip, self.port, self.timeout).connect()
            self.conn.disable_device()  # Typically, you disable a device to perform operations safely
            return True
        except Exception as e:
            print(f"Error connecting to device: {e}")
            return False
        
    def get_attendance(self):
        """Fetches attendance records from the device."""
        if self.conn:
            try:
            # Fetch attendance records directly from the device connection
                attendance_records = self.conn.get_attendance()
            
            # Debugging: Print the type of the attendance_records to understand what it is
                print("Type of attendance_records:", type(attendance_records))
            # If it's an iterable of custom objects, you might want to see the first element (if not empty)
                if attendance_records:  # Ensure it is not empty
                    print("Properties of first record:", dir(attendance_records[0]))

            # Process records if they are in a known iterable format
                attendance_data = []
                for record in attendance_records:
                # Adapt these lines based on the actual methods/properties found
                    attendance_data.append({
                        "timestamp": record.timestamp,  # Adjust if the attribute name differs
                        "status": record.status,        # Adjust if the attribute name differs
                        "error_code": getattr(record, 'error_code', 0),
                        "user_id": record.user_id       # Adjust if the attribute name differs
                })
                return attendance_data
            except Exception as e:
                print(f"Get attendance error: {e}")
                return []
        else:
            print("Device not connected")
            return []

    def get_formatted_att_record(self):
        print(format_attendance_records(attendance_records))



    def set_user_info(self, uid, name, privilege, password, group_id, user_id, card, department=None, role=None, fingerprints=None):
        if not self.conn:
            print("Device not connected.")
            return False
        try:
            self.conn.set_user(uid=uid, name=name, privilege=privilege, password=password, group_id=group_id, user_id=user_id, card=card)
            print(f"User {user_id} ({name}) set successfully.")
            return True
        except Exception as e:
            print(f"Error setting user information: {e}")
            return False

            

    def disconnect(self):
        if self.conn:
            self.conn.enable_device()  # Enable the device before disconnecting
            self.conn.disconnect()

# Load user data from a JSON file
def load_users_from_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    enrollment_system = Enrollment(ip="192.168.0.201", port=4370)
    if enrollment_system.connect():
        print("Connected to the device successfully.")
        
        # Attempt to fetch attendance data
        attendance_records = enrollment_system.get_attendance()
        if attendance_records:
            print("Attendance Records Fetched:", attendance_records)
        else:
            print("No attendance records available or error occurred.")

        # Load and set users
        users = load_users_from_json('users.json')
        for user in users:
            if enrollment_system.set_user_info(**user):
                print(f"User information for {user['name']} ({user['user_id']}) set successfully.")
            else:
                print("Failed to set user information.")

        enrollment_system.disconnect()
    else:
        print("Failed to connect to the device.")

    rec = enrollment_system.get_formatted_att_record()
    print(rec)