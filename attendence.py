from zk import ZK, const
import json
from utility import write_to_db, format_attendance_records

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

    def disconnect(self):
        """ Disconnect from the device """
        if self.conn:
            self.conn.enable_device()
            self.conn.disconnect()

    @staticmethod
    def create_device_connection(ip_address, port=4370, timeout=5):
        """Establishes connection to the ZKTeco device."""
        zk = ZK(ip_address, port=port, timeout=timeout)
        try:
            conn = zk.connect()
            conn.disable_device()  # Disable the device to perform operations
            return conn
        except Exception as e:
            print(f"Error connecting to device: {e}")
            return None

    def get_attendance(self, user_id=None):
        """Fetch attendance records from the device, optionally filtered by a user_id."""
        if not self.conn:
            print("Device not connected: Error 202")
            return []

        attendance_records = []
        try:
            attendance = self.conn.get_attendance()
            print(attendance)
            for record in attendance:
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


