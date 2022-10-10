from ctypes import c_bool
import multiprocessing as mp

from processor import ConnectModProcess

from DB_connect import createConnection


def get_connect_db():
    try:
        connection_db = createConnection()
        cursor_db = connection_db.cursor()
        return [connection_db, cursor_db]
    except:
        return False


def start_process(data_proc:dict):
    try:
        status = mp.Value(c_bool, False)
        stop = mp.Value(c_bool, False)
        process = ConnectModProcess(
            name_connect=data_proc['name'],
            ip=data_proc['ip'],
            port=data_proc['port'],
            status=status,
            stop_point=stop,
            values=data_proc['type_mashine']
        )
        process.start()
    except:
        process = None
        status = None
        stop = None
    return [process, status, stop]


def stop_process(process_object: dict):
    while process_object['process'].is_alive():
        process_object['process'].terminate()
        process_object['stop_point'].value = True
    return True


def get_type_value(id: int, cur):
    cur.execute(f"""
                SELECT value FROM type_mashine
                    WHERE id={id}
                        LIMIT 1
                """)
    value, = cur.fetchone()
    return value


def get_connections(con, cur):
    connections = []
    cur.execute("""
               SELECT id, name, module, ip, port, type_mashine_id FROM mashine order by id
               """)    
    for id, name, module, ip, port, type_id in cur.fetchall():
        type_value = get_type_value(type_id, cur)
        connect = {
            "id": id,
            "name": name,
            "module": module,
            "ip": ip,
            "port": port,
            "type_mashine": generate_value(type_value),
        }
        connections.append(connect)
    return connections


def update_global_connections(old_connections: list, new_connections: list, work_process: dict, restart_list: list):
    for index, old_connect in enumerate(old_connections):
        if not old_connect in new_connections:
            ############################################################
            old_connections.pop(index)
            if old_connect in restart_list:
                restart_list.pop(restart_list.index(old_connect))
            status = stop_process(work_process[old_connect['name']])
            if status:
                del work_process[old_connect['name']]
              ##################
             ## STOP PROCESS ##
            ##################
            ############################################################
    for index, new_connect in enumerate(new_connections):
        if not new_connect in old_connections:
            old_connections.append(new_connect)
            ############################################################
            proc, status, stop = start_process(new_connect)
            if proc:
                work_process[new_connect['name']] = {
                    'process': proc,
                    'status': status,
                    'stop_point': stop
                }
            else:
                if not new_connect in restart_list:
                    restart_list.append(new_connect)
              ###################
             ## START PROCESS ##
            ###################
            ############################################################


def restart_process(restart_list, work_process):
    for index, connect in enumerate(restart_list):
        proc, status, stop = start_process(connect)
        if proc:
            work_process[connect['name']] = {
                'process': proc,
                'status': status,
                'stop_point': stop
            }
            restart_list.pop(index)


def generate_value(value: int):
    data = {
        "value_list": [
            {
                "name": "status_power_mashine",
                "type_table": "bool",
                "type_val": "bool",
                "signed": False,
                "big_or_little_endian": True,
                "byte_swap": False,
                "start": 0,
                "min_time_check": 1000,
                "max_time_check": 1,
                "if_change": True,
                "divide": False,
                "divide_num": 1,
                "bit": 0
            },
            {
                "name": "status_work_mashine",
                "type_table": "bool",
                "type_val": "bool",
                "signed": False,
                "big_or_little_endian": True,
                "byte_swap": False,
                "start": 0,
                "min_time_check": 1000,
                "max_time_check": 1,
                "if_change": True,
                "divide": False,
                "divide_num": 1,
                "bit": 1
            }
        ]
    }
    if value == 1 or value == 8 or value == 9 or value == 14 or value == 16:
        data["value_list"].append(
            {
                "name": "count_processed_parts",
                "type_table": "double",
                "type_val": "double",
                "signed": False,
                "big_or_little_endian": True,
                "byte_swap": False,
                "start": 2,
                "min_time_check": 1000,
                "max_time_check": 1,
                "if_change": True,
                "divide": False,
                "divide_num": 1,
            }
        )
        if value == 1:
            data["name"] = "skipper"
            data["slave_id"] = 1
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
        if value == 8:
            data["name"] = "bima_410v"
            data["slave_id"] = 1
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
        if value == 9:
            data["name"] = "rover_s1_30"
            data["slave_id"] = 1
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
        if value == 14:
            data["name"] = "biesse_techno_ftd"
            data["slave_id"] = 1
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
        if value == 16:
            data["name"] = "biesse_ftd_cn"
            data["slave_id"] = 1
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
    elif value == 2 or value == 3 or value == 4 or value == 5 or value == 12 or value == 13:
        data["value_list"].append(
            {
                "name": "count_facings",
                "type_table": "double",
                "type_val": "double",
                "signed": False,
                "big_or_little_endian": True,
                "byte_swap": False,
                "start": 2,
                "min_time_check": 1000,
                "max_time_check": 1,
                "if_change": True,
                "divide": False,
                "divide_num": 1
            }
        )
        data["value_list"].append(
            {
                "name": "conveyor_speed",
                "type_table": "double",
                "type_val": "double",
                "signed": False,
                "big_or_little_endian": True,
                "byte_swap": False,
                "start": 4,
                "min_time_check": 1000,
                "max_time_check": 1,
                "if_change": True,
                "divide": False,
                "divide_num": 1
            }
        )
        if value == 2:
            data["name"] = "ima_novimat_l20"
            data["slave_id"] = 2
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
        if value == 3:
            data["name"] = "ima_novimat_l12"
            data["slave_id"] = 2
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
        if value == 4:
            data["name"] = "ima_novimat_r3_plus"
            data["slave_id"] = 2
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
        if value == 5:
            data["name"] = "ima_novimat_r3"
            data["slave_id"] = 2
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
        if value == 12:
            data["name"] = "ima_combivis_l12"
            data["slave_id"] = 2
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
        if value == 13:
            data["name"] = "ima_combivis_r3"
            data["slave_id"] = 2
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
    if value == 6 or value == 7 or value == 10:
        data["value_list"].append(
            {
                "name": "count_processed_boards",
                "type_table": "double",
                "type_val": "double",
                "signed": False,
                "big_or_little_endian": True,
                "byte_swap": False,
                "start": 2,
                "min_time_check": 1000,
                "max_time_check": 1,
                "if_change": True,
                "divide": False,
                "divide_num": 1
            }
        )
        if value == 6:
            data["name"] = "holzma_hpp"
            data["slave_id"] = 3
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
        if value == 7:
            data["name"] = "schelling_fh4"
            data["slave_id"] = 3
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
        if value == 10:
            data["name"] = "holzma_hkl11"
            data["slave_id"] = 3
            data["func"] = 3
            data["start_reg_adr"] = 0
            data["size"] = 6
    if value == 11:
        data["name"] = "unimak"
        data["slave_id"] = 4
        data["func"] = 3
        data["start_reg_adr"] = 0
        data["size"] = 4
    if value == 15:
        data["name"] = "homag"
        data["slave_id"] = 4
        data["func"] = 3
        data["start_reg_adr"] = 0
        data["size"] = 4
    data = [data]
    return data


def write_status_connect(cursore, connect, name_connection, status):
    cursore.execute(f"""
                        UPDATE mashine
                            SET status_connect={status}
                                WHERE name='{name_connection}'
                    """)
    connect.commit()