from zk import ZK, const
from base import ZKBase

class ZKFacade:
    def __init__(self, ip, port=4370, timeout=60, password=0, force_udp=False, omit_ping=False, verbose=False, encoding='UTF-8'):
        self.zk_base = ZKBase(ip, port, timeout, password, force_udp, omit_ping, verbose, encoding)

    def connect(self):
        return self.zk_base.connect()

    def delete_user_template(self, uid=0, temp_id=0, user_id=''):
        return self.zk_base.delete_user_template(uid, temp_id, user_id)

    def disable_device(self):
        return self.zk_base.disable_device()

    def disconnect(self):
        return self.zk_base.disconnect()

    def enable_device(self):
        return self.zk_base.enable_device()

    def enroll_user(self, uid=0, temp_id=0, user_id=''):
        return self.zk_base.enroll_user(uid, temp_id, user_id)

    def free_data(self):
        return self.zk_base.free_data()

    def get_attendance(self):
        return self.zk_base.get_attendance()

    def get_compat_old_firmware(self):
        return self.zk_base.get_compat_old_firmware()

    def get_device_name(self):
        return self.zk_base.get_device_name()

    def get_extend_fmt(self):
        return self.zk_base.get_extend_fmt()

    def get_face_fun_on(self):
        return self.zk_base.get_face_fun_on()

    def get_face_version(self):
        return self.zk_base.get_face_version()

    def get_firmware_version(self):
        return self.zk_base.get_firmware_version()

    def get_fp_version(self):
        return self.zk_base.get_fp_version()

    def get_mac(self):
        return self.zk_base.get_mac()

    def get_network_params(self):
        return self.zk_base.get_network_params()

    def get_pin_width(self):
        return self.zk_base.get_pin_width()

    def get_platform(self):
        return self.zk_base.get_platform()

    def get_serialnumber(self):
        return self.zk_base.get_serialnumber()

    def get_templates(self):
        return self.zk_base.get_templates()

    def get_time(self):
        return self.zk_base.get_time()

    def get_user_extend_fmt(self):
        return self.zk_base.get_user_extend_fmt()

    def get_user_template(self, uid, temp_id=0, user_id=''):
        return self.zk_base.get_user_template(uid, temp_id, user_id)

    def get_users(self):
        return self.zk_base.get_users()

    def set_sdk_build_1(self):
        return self.zk_base.set_sdk_build_1()

    def set_time(self, timestamp):
        return self.zk_base.set_time(timestamp)

    def set_user(self, uid=None, name='', privilege=0, password='', group_id='', user_id='', card=0):
        return self.zk_base.set_user(uid, name, privilege, password, group_id, user_id, card)

    def test_voice(self, index=0):
        return self.zk_base.test_voice(index)

    def test_ping(self):
        return self.zk_base.test_ping()

    def test_tcp(self):
        return self.zk_base.test_tcp()

    def test_udp(self):
        return self.zk_base.test_udp()

    def make_commkey(self, key, session_id, ticks=50):
        return self.zk_base.make_commkey(key, session_id, ticks)

    def safe_cast(self, val, to_type, default=None):
        return self.zk_base.safe_cast(val, to_type, default)
