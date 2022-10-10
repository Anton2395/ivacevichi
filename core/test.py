import time
import multiprocessing as _mp
from ctypes import c_bool

from processor import ConnectModProcess

if __name__ == '__main__':
    data = [{
        "name": "test_slave_id_1",
        "slave_id": 2,
        "func": 3,
        "start_reg_adr": 0,
        "size": 6,
        "value_list": [
            {
                "name": "conveyor_speed",
                "type_table": "double",
                "type_val": "double",
                "signed": False,
                "big_or_little_endian": True,
                "byte_swap": False,
                "start": 4,
                "min_time_check": 1000,
                "max_time_check": 60,
                "if_change": True,
                "divide": False,
                "divide_num": 1
            },
        ]
    }]
    status = _mp.Value(c_bool, False)
    stop = _mp.Value(c_bool, False)
    proc = ConnectModProcess(name_connect="test_madtcp", ip="192.168.1.136", port=502, status=status, stop_point=stop, values=data)
    proc.start()
    for i in range(30):
        time.sleep(1)
        print(status.value, stop.value)
    proc.terminate()