from zk import ZK, const
import json
from utility import write_to_db, format_attendance_records

class Enrollment:
    def __init__(self, ip, port=4370, timeout=5):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.conn = None

    def connect(self):
        """Connect to the ZKTeco device."""
        try:
            self.conn = ZK(self.ip, port=self.port, timeout=self.timeout).connect()
            self.conn.disable_device()
            return True
        except Exception as e:
            print(f"Error connecting to device: {e}")
            return False

    def enroll_user(self, uid=0, temp_id=0, user_id=''):
        """Starts the enrollment process for a user on the ZKTeco device.

        Parameters:
        uid (int): The user's ID on the device.
        temp_id (int): The fingerprint template ID (typically 0 to 9).
        user_id (str): The user's identification number as a string.

        Returns:
        bool: True if successful, False otherwise.
        """
        if not self.conn:
            print("Device not connected.")
            return False

        try:
            # Assuming self.conn has a method to enroll a user; this might need to be adjusted
            # based on your device's capabilities and the pyzk library's documentation.
            response = self.conn.set_user(uid=uid, name=user_id, privilege=const.USER_DEFAULT, password='', group_id='', user_id=user_id)
            if response:
                print(f"User {user_id} enrollment started successfully.")
                # Depending on the device's process, you might need to capture fingerprints here.
                return True
            else:
                print("Failed to start enrollment process.")
                return False
        except Exception as e:
            print(f"Error enrolling user: {e}")
            return False



    def set_user_info(self, uid=None, name='', privilege=0, password='', group_id='', user_id='', card=0):
        """Create or update user information on the ZKTeco device.

        Parameters:
        uid (int): User ID on the device. If None, a new user will be created.
        name (str): Name of the user.
        privilege (int): User privilege (refer to const.py for values).
        password (str): User password.
        group_id (str): Group ID.
        user_id (str): Your own user ID.
        card (int): Card number associated with the user.

        Returns:
        bool: True if successful, False otherwise.
        """
        if not self.conn:
            print("Device not connected.")
            return False

        try:
            # Use the pyzk set_user method to create or update the user
            self.conn.set_user(uid=uid, name=name, privilege=privilege, password=password, group_id=group_id, user_id=user_id, card=card)
            print(f"User {user_id} ({name}) set successfully.")
            return True
        except Exception as e:
            print(f"Error setting user information: {e}")
            return False

    def save_user_template(self, user, fingers=[]):
        """Save user fingerprint templates to the ZKTeco device.

        Parameters:
        user (dict): User information including at least 'uid'.
        fingers (list): List of fingerprints. Each fingerprint is a dict with 'fid' (finger index) and 'template'.
                        The 'fid' ranges from 0-9.
        """
        if not self.conn:
            print("Device not connected.")
            return False

        try:
            uid = user.get('uid')
            if uid is None:
                print("User UID is required.")
                return False

            for finger in fingers:
                fid = finger.get('fid')
                template = finger.get('template')
                if fid is None or template is None:
                    print("Finger ID and template are required for each finger.")
                    continue

                # Assuming 'set_user_template' is a method provided by the device or pyzk library
                # to set a fingerprint template for a specific finger of a user.
                # You will need to replace it with the actual method supported by your device.
                self.conn.set_user_template(uid=uid, fid=fid, template=template)

            print(f"Templates saved for user UID: {uid}")
            return True
        except Exception as e:
            print(f"Error saving user templates: {e}")
            return False


    def delete_user(self, uid=0, user_id=''):
        """Delete a specific user by uid or user_id.

        Parameters:
        uid (int): User ID that is generated from the device.
        user_id (str): Your own user ID.

        Returns:
        bool: True if successful, False otherwise.
        """
        if not self.conn:
            print("Device not connected.")
            return False

        try:
            # Check which identifier is provided and perform deletion accordingly
            if uid:
                # Assuming delete_user is the method to delete a user by UID
                # This needs to be replaced with the actual method name and parameters as per your device's SDK or pyzk library
                response = self.conn.delete_user(uid=uid)
            elif user_id:
                # If your device or library supports deletion by user_id, use the corresponding method
                # This is a placeholder and needs to be adjusted based on actual capabilities
                response = self.conn.delete_user(user_id=user_id)
            else:
                print("No valid user identifier provided.")
                return False

            if response:
                print(f"User deleted successfully. UID: {uid}, User ID: {user_id}")
                return True
            else:
                print("Failed to delete user.")
                return False
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    def disconnect(self):
        """Disconnect from the ZKTeco device."""
        if self.conn:
            self.conn.enable_device()
            self.conn.disconnect()

enrollment_system = Enrollment(ip="192.168.0.201", port=4370, timeout=5)
if enrollment_system.connect():
    print("Connected to the device successfully.")
else:
    print("Failed to connect to the device.")
    # Exit or handle connection failure appropriately
# Example user information
uid = 1  # Device-specific numeric user ID, adjust as needed
name = "userTest"
privilege = const.USER_DEFAULT  # Use appropriate privilege level
password = ""  # Assuming no password is set
group_id = "8055"  # Assuming no group ID is set
user_id = "8089"  # A custom string user ID
card = 1043801067  # Assuming no card is used

# Set or update the user information
success = enrollment_system.set_user_info(uid, name, privilege, password, group_id, user_id, card)
if success:
    print(f"User information for {name} ({user_id}) set successfully.")
else:
    print("Failed to set user information.")
enrollment_system.disconnect()
