import time
from service import get_connections, update_global_connections, start_process, restart_process, write_status_connect, get_connect_db
from psycopg2 import OperationalError, InterfaceError
from loguru import logger



print('Connect to DB ...')
db_data = get_connect_db()
if db_data:
    connection_db = db_data[0]
    cursor_db = db_data[1]
print('DONE')


global_connections = []
work_proc = {}
restart_list = []
STATUS_LIST = {}
print('Generate connections object ...') 
global_connections = get_connections(connection_db, cursor_db)
print('DONE')

print('Start processes ...')
for con in global_connections:
    proc, status, stop = start_process(con)
    # print(proc)
    if proc:
        work_proc[con['name']] = {
            'process': proc,
            'status': status,
            'stop_point': stop
        }
        STATUS_LIST[con['name']] = status.value
    else:
        restart_list.append(con)
print('DONE')


print('-----------------------------------------')
print('-----------------------------------------')
# print('work: ', work_proc)

while True:
    try:
        new_connections = get_connections(connection_db, cursor_db)
        if global_connections != new_connections:
            update_global_connections(global_connections, new_connections, work_proc, restart_list)
        for key in work_proc:
            write_status_connect(
                connect=connection_db,
                cursore=cursor_db,
                name_connection=key,
                status=work_proc[key]['status'].value
            )
            print(f'status {key}: ', work_proc[key]['status'].value)
        restart_process(restart_list=restart_list, work_process=work_proc)
        time.sleep(1)
    except OperationalError:
        logger.error("BAD DB CONNECT")
    except InterfaceError:
        logger.error("BAD DB CONNECT")
        time.sleep(5)
        db_data = get_connect_db()
        if db_data:
            connection_db = db_data[0]
            cursor_db = db_data[1]
        