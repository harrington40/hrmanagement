from zk import ZK, const

from utility import write_to_db
from utility import format_attendance_records
class Attendance:
    def __init__(self, ip, port=4370, timeout=5):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.conn = None

    def connect(self):
        """ Connect to the ZKTeco device """
        try:
            self.conn = ZK(self.ip, port=self.port, timeout=self.timeout).connect()
            self.conn.disable_device()
            return True
        except Exception as e:
            print(f"Error connecting to device: {e}")
            return False

    def get_firmware_version(self):
        """ Get firmware version of the device """
        try:
            if self.conn:
                return self.conn.get_firmware_version()
            return None
        except Exception as e:
            print(f"Error getting firmware version: {e}")
            return None

    def get_all_users(self):
        """ Get all users in JSON format """
        try:
            if self.conn:
                users = self.conn.get_users()

                # Create a list to store user data in JSON format
                users_json = []

                for user in users:
                    user_data = {
                        'uid': user.uid,
                        'name': user.name,
                        'privilege': 1 if user.privilege == const.USER_ADMIN else 0,
                        'password': user.password,
                        'group_id': user.group_id,
                        'user_id': user.user_id
                    }
                    # Append each user's data to the list in JSON format
                    users_json.append(user_data)

                return users_json

        except Exception as e:
            print(f"Error getting all users: {e}")
            return None

    def get_user(self, user_id):
        """ Get a specified user by user ID in JSON format """
        try:
            if self.conn:
                users = self.conn.get_users()

                if user_id == '0':
                    # Return all users as a list of dictionaries in JSON format
                    return self.get_all_users()

                for user in users:
                    if user.user_id == user_id:
                        user_data = {
                            'uid': user.uid,
                            'name': user.name,
                            'privilege': 'Admin' if user.privilege == const.USER_ADMIN else 'User',
                            'password': user.password,
                            'group_id': user.group_id,
                            'user_id': user.user_id
                        }
                        return user_data

            # User not found
            return None

        except Exception as e:
            print(f"Error getting specified user: {e}")
            return None

    def test_voice(self):
        """ Perform voice test """
        try:
            if self.conn:
                self.conn.test_voice()
        except Exception as e:
            print(f"Error in voice test: {e}")

    def disconnect(self):
        """ Disconnect from the device """
        if self.conn:
            self.conn.enable_device()
            self.conn.disconnect()
    
    def read_fingerprint(self, user_id_from_device):
        try:
            if self.conn:
                # Retrieve the fingerprint template for the specified user
                user_templates = self.conn.get_user_template(uid=user_id_from_device)

                if user_templates:
                    # Fingerprint data retrieved successfully
                    print(f"Fingerprint retrieved for user ID from device: {user_id_from_device}")

                    # Process the fingerprint data as needed
                    for finger_index, fingerprint_template in enumerate(user_templates):
                        # Save fingerprint template data to a file
                        filename = f"user_{user_id_from_device}_finger_{finger_index + 1}.fpt"
                        with open(filename, 'wb') as file:
                            file.write(fingerprint_template)
                            print(f"Fingerprint saved to {filename}")

                else:
                    print(f"No fingerprint data found for user ID from device: {user_id_from_device}")
            else:
                print("Device not connected.")
        except Exception as e:
            print(f"Error reading fingerprint: {e}")


    def verify_fingerprint_existence(self, user_id_from_device):
        """Verify if a fingerprint exists for a specified user ID."""
        try:
            if self.conn:
                user_templates = self.conn.get_user_template(uid=user_id_from_device)
                if user_templates:
                    print(f"Fingerprint(s) found for user ID from device: {user_id_from_device}. Total fingerprints: {len(user_templates)}")
                    return True
                else:
                    print(f"No fingerprint data found for user ID from device: {user_id_from_device}")
                    return False
            else:
                print("Device not connected.")
                return False
        except Exception as e:
            print(f"Error verifying fingerprint existence: {e}")
            return False
        

    def get_attendance(self, user_id=None):
        """Fetch attendance records from the device, optionally filtered by a user_id.

        Args:
            user_id (str, optional): The user ID to filter attendance records. If None, all records are fetched.

        Returns:
            list: A list of dictionaries, each containing a user_id, timestamp, and status of an attendance record.
        """
        if not self.conn:
            print("Device not connected")
            return []

        attendance_records = []
        try:
            # Fetch attendance data
            attendance = self.conn.get_attendance()
            for record in attendance:
                # Check if a user_id filter is applied
                if user_id is None or record.user_id == user_id:
                    attendance_records.append({
                        'user_id': record.user_id,
                        'timestamp': record.timestamp,
                        'status': record.status
                    })
            return format_attendance_records(attendance_records)

        except Exception as e:
            print(f"Error fetching attendance data: {e}")
            return []


    def get_user_data_with_attendance(self, user):
        """
        Fetches detailed user data including attendance records.

        Args:
            user (dict): A dictionary containing basic user info.

        Returns:
            dict: Extended user data including formatted attendance records.
        """
    # Basic user data structure
        user_data = {
            'uid': user['uid'],
            'name': user['name'],
            'privilege': 1 if user['privilege'] == 'Admin' else 0,
            'password': user['password'],
            'group_id': user['group_id'],
            'user_id': user['user_id']
        }
    
        # Fetch attendance records for the user
        attendance_records = self.get_attendance(user_id = 1)
    
        # Format the attendance records for display or further processing
        formatted_attendance_records = format_attendance_records(attendance_records)
    
        
        # Add the formatted attendance records to the user data
        user_data['attendance'] = formatted_attendance_records
    
        return user_data


# Example usage
attendance_system = Attendance('192.168.0.201', port=4370)

if attendance_system.connect():
    specified_user_id = 1  # Replace with the user ID generated from the device
    attendance_system.read_fingerprint(specified_user_id)
    user = attendance_system.get_user(specified_user_id)
    if user:
        print(f"User Found: {user}")
    else:
        print("User not found.")

    attendance_system.disconnect()
else:
    print("Failed to connect to the ZKTeco device.")

if attendance_system.connect():
    all_users = attendance_system.get_all_users()
    if all_users:
        for user in all_users:
            print(f"User Found: {user}")

           
            # Define your SQL insert query with the actual table name and columns
            insert_query = "INSERT IGNORE INTO ClockInOut (uid, name, privilege, password, group_id, user_id) \
               VALUES (%s, %s, %s, %s, %s, %s)"


            # Create a tuple with the values extracted from the user_data dictionary
            data = ( user['uid'], user['name'], user['privilege'], user['password'], user['group_id'], user['user_id'])

            # Insert the user data into the database
            write_to_db(insert_query, data)

    else:
        print("No users found in the system.")
else:
    print("Failed to connect to the ZKTeco device.")
specified_user_id = 1
if attendance_system.verify_fingerprint_existence(specified_user_id):
    print("Fingerprint exists for specified user.")
else:
    print("No fingerprint found for specified user.")
    attendance_system.disconnect()
    attendance_system.connect()

if attendance_system.connect():
    attendance_records = attendance_system.get_attendance(user_id =None)
    for record in attendance_records:
        print(record)
   
else:
    print("Failed to connect to the device.")

user = {'uid': '123', 'name': 'John Doe', 'privilege': 'Admin', 'password': 'password123', 'group_id': '1', 'user_id': '123'}
user_data_with_attendance = attendance_system.get_user_data_with_attendance(user)
print(user_data_with_attendance)
attendance_system.disconnect()