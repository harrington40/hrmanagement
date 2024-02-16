from cmath import e
import sys
from typing import Any
from zk import ZK, const

conn = None
zk = ZK('192.168.0.201', port=4370, timeout=5)

try:
    print('Connecting to device ...')
    conn = zk.connect()
    print('Disabling device ...')
    conn.disable_device()
    print('Firmware Version: : {}'.format(conn.get_firmware_version()))

    # Get users
    users = conn.get_users()
    for user in users:
        privilege = 'User'
        if user.privilege == const.USER_ADMIN:
            privilege = 'Admin'

        print('- UID #{}'.format(user.uid))
        print('  Name       : {}'.format(user.name))
        print('  Privilege  : {}'.format(privilege))
        print('  Password   : {}'.format(user.password))
        print('  Group ID   : {}'.format(user.group_id))
        print('  User  ID   : {}'.format(user.user_id))

    print("Voice Test ...")
    conn.test_voice()

except Exception as e:
    print("An error occurred: ", e)

finally:
    if conn:
        print('Enabling device ...')
        conn.enable_device()
        conn.disconnect()
