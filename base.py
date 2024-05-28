from zk import ZK, const

class ZKBase:
    def __init__(self, ip, port=4370, timeout=60, password=0, force_udp=False, omit_ping=False, verbose=False, encoding='UTF-8'):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.password = password
        self.force_udp = force_udp
        self.omit_ping = omit_ping
        self.verbose = verbose
        self.encoding = encoding
        self.device = None

    def connect(self):
        try:
            self.device = ZK(self.ip, port=self.port, timeout=self.timeout, password=self.password,
                             force_udp=self.force_udp, omit_ping=self.omit_ping, verbose=self.verbose, encoding=self.encoding)
            self.device.connect()
            return True
        except Exception as e:
            print(f"Connection error: {str(e)}")
            return False

    # Other methods from the previous implementation...

    def delete_user_template(self, uid=0, temp_id=0, user_id=''):
        if self.device:
            try:
                if uid and temp_id:
                    self.device.delete_user_template(uid, temp_id)
                elif user_id and temp_id:
                    self.device.delete_user_template(uid=user_id, temp_id=temp_id)
                else:
                    print("Provide uid and temp_id or user_id and temp_id to delete the template")
                    return False
                return True
            except Exception as e:
                print(f"Delete user template error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def disable_device(self):
        if self.device:
            try:
                self.device.disable_device()
                return True
            except Exception as e:
                print(f"Disable device error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def disconnect(self):
        if self.device:
            try:
                self.device.disconnect()
                return True
            except Exception as e:
                print(f"Disconnect error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def enable_device(self):
        if self.device:
            try:
                self.device.enable_device()
                return True
            except Exception as e:
                print(f"Enable device error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def enroll_user(self, uid=0, temp_id=0, user_id=''):
        if self.device:
            try:
                if uid and temp_id and user_id:
                    self.device.enroll_user(uid, temp_id, user_id)
                else:
                    print("Provide uid, temp_id, and user_id to enroll the user")
                    return False
                return True
            except Exception as e:
                print(f"Enroll user error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def free_data(self):
        if self.device:
            try:
                self.device.free_data()
                return True
            except Exception as e:
                print(f"Free data error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def get_attendance(self):
        if self.device:
            try:
                attendance_records = self.device.get_attendance()
                return attendance_records
            except Exception as e:
                print(f"Get attendance error: {str(e)}")
                return []
        else:
            print("Device not connected")
            return []

    def get_compat_old_firmware(self):
        if self.device:
            try:
                compatibility = self.device.get_compat_old_firmware()
                return compatibility
            except Exception as e:
                print(f"Get compatibility with old firmware error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def get_device_name(self):
        if self.device:
            try:
                device_name = self.device.get_device_name()
                return device_name
            except Exception as e:
                print(f"Get device name error: {str(e)}")
                return ""
        else:
            print("Device not connected")
            return ""

    def get_extend_fmt(self):
        if self.device:
            try:
                extend_fmt = self.device.get_extend_fmt()
                return extend_fmt
            except Exception as e:
                print(f"Get extend format error: {str(e)}")
                return ""
        else:
            print("Device not connected")
            return ""

    def get_face_fun_on(self):
        if self.device:
            try:
                face_fun_on = self.device.get_face_fun_on()
                return face_fun_on
            except Exception as e:
                print(f"Get face function status error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def get_face_version(self):
        if self.device:
            try:
                face_version = self.device.get_face_version()
                return face_version
            except Exception as e:
                print(f"Get face version error: {str(e)}")
                return ""
        else:
            print("Device not connected")
            return ""

    def get_firmware_version(self):
        if self.device:
            try:
                firmware_version = self.device.get_firmware_version()
                return firmware_version
            except Exception as e:
                print(f"Get firmware version error: {str(e)}")
                return ""
        else:
            print("Device not connected")
            return ""

    def get_fp_version(self):
        if self.device:
            try:
                fp_version = self.device.get_fp_version()
                return fp_version
            except Exception as e:
                print(f"Get fingerprint version error: {str(e)}")
                return ""
        else:
            print("Device not connected")
            return ""

    def get_mac(self):
        if self.device:
            try:
                mac_address = self.device.get_mac()
                return mac_address
            except Exception as e:
                print(f"Get MAC address error: {str(e)}")
                return ""
        else:
            print("Device not connected")
            return ""

    def get_network_params(self):
        if self.device:
            try:
                network_params = self.device.get_network_params()
                return network_params
            except Exception as e:
                print(f"Get network parameters error: {str(e)}")
                return {}
        else:
            print("Device not connected")
            return {}


    def get_pin_width(self):
        if self.device:
            try:
                pin_width = self.device.get_pin_width()
                return pin_width
            except Exception as e:
                print(f"Get PIN width error: {str(e)}")
                return ""
        else:
            print("Device not connected")
            return ""

    def get_platform(self):
        if self.device:
            try:
                platform_name = self.device.get_platform()
                return platform_name
            except Exception as e:
                print(f"Get platform name error: {str(e)}")
                return ""
        else:
            print("Device not connected")
            return ""

    def get_serialnumber(self):
        if self.device:
            try:
                serial_number = self.device.get_serialnumber()
                return serial_number
            except Exception as e:
                print(f"Get serial number error: {str(e)}")
                return ""
        else:
            print("Device not connected")
            return ""

    def get_templates(self):
        if self.device:
            try:
                templates = self.device.get_templates()
                return templates
            except Exception as e:
                print(f"Get templates error: {str(e)}")
                return []
        else:
            print("Device not connected")
            return []

    def get_time(self):
        if self.device:
            try:
                machine_time = self.device.get_time()
                return machine_time
            except Exception as e:
                print(f"Get machine time error: {str(e)}")
                return ""
        else:
            print("Device not connected")
            return ""

    def get_user_extend_fmt(self):
        if self.device:
            try:
                user_extend_fmt = self.device.get_user_extend_fmt()
                return user_extend_fmt
            except Exception as e:
                print(f"Get user extend format error: {str(e)}")
                return ""
        else:
            print("Device not connected")
            return ""

    def get_user_template(self, uid, temp_id=0, user_id=''):
        if self.device:
            try:
                if uid and temp_id:
                    user_templates = self.device.get_user_template(uid, temp_id)
                elif user_id and temp_id:
                    user_templates = self.device.get_user_template(uid=user_id, temp_id=temp_id)
                else:
                    print("Provide uid and temp_id or user_id and temp_id to get user templates")
                    return []
                return user_templates
            except Exception as e:
                print(f"Get user templates error: {str(e)}")
                return []
        else:
            print("Device not connected")
            return []

    def get_users(self):
        if self.device:
            try:
                users = self.device.get_users()
                return users
            except Exception as e:
                print(f"Get users error: {str(e)}")
                return []
        else:
            print("Device not connected")
            return []

    # Add the remaining methods from the previous implementation...

    def set_sdk_build_1(self):
        if self.device:
            try:
                self.device.set_sdk_build_1()
                return True
            except Exception as e:
                print(f"Set SDK build 1 error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def set_time(self, timestamp):
        if self.device:
            try:
                self.device.set_time(timestamp)
                return True
            except Exception as e:
                print(f"Set device time error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def set_user(self, uid=None, name='', privilege=0, password='', group_id='', user_id='', card=0):
        if self.device:
            try:
                self.device.set_user(uid, name, privilege, password, group_id, user_id, card)
                return True
            except Exception as e:
                print(f"Set user error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False


    def test_voice(self, index=0):
        if self.device:
            try:
                self.device.test_voice(index)
                return True
            except Exception as e:
                print(f"Test voice error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def test_ping(self):
        import os
        if self.device:
            try:
                response = os.system(f"ping -c 1 {self.ip}")
                return response == 0
            except Exception as e:
                print(f"Test ping error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def test_tcp(self):
        if self.device:
            try:
                self.device.test_tcp()
                return True
            except Exception as e:
                print(f"Test TCP connection error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    def test_udp(self):
        if self.device:
            try:
                self.device.test_udp()
                return True
            except Exception as e:
                print(f"Test UDP connection error: {str(e)}")
                return False
        else:
            print("Device not connected")
            return False

    @staticmethod
    def make_commkey(key, session_id, ticks=50):
        try:
            from zk import make_commkey
            return make_commkey(key, session_id, ticks)
        except Exception as e:
            print(f"Make commkey error: {str(e)}")
            return None

    @staticmethod
    def safe_cast(val, to_type, default=None):
        try:
            return to_type(val)
        except (ValueError, TypeError):
            return default

# Assuming the ZKBase class is properly defined and imported as discussed earlier

# Create an instance of ZKBase


