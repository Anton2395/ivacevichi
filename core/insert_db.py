import datetime
from random import randint

from DB_connect import createConnection


con = createConnection()
cursor = con.cursor()

table_name_list = [
    "mvlab_test_ima_ima_novimat_l20_status_work_mashine",
    "mvlab_test_shkiper_skipper_status_work_mashine",
    "mvlab_test_value_11_unimak_status_work_mashine",
    "mvlab_test_value_12_ima_combivis_l12_status_work_mashine",
    "mvlab_test_value_13_ima_combivis_r3_status_work_mashine",
    "mvlab_test_value_14_biesse_techno_ftd_status_work_mashine",
    "mvlab_test_value_15_homag_status_work_mashine",
    "mvlab_test_value_16_biesse_ftd_cn_status_work_mashine",
    "mvlab_test_value_3_ima_novimat_l12_status_work_mashine",
    "mvlab_test_value_4_ima_novimat_r3_plus_status_work_mashine",
    "mvlab_test_value_5_ima_novimat_r3_status_work_mashine",
    "mvlab_test_value_6_holzma_hpp_status_work_mashine",
    "mvlab_test_value_7_schelling_fh4_status_work_mashine",
    "mvlab_test_value_8_bima_410v_status_work_mashine",
    "mvlab_test_value_9_rover_s1_30_status_work_mashine"
]

start = datetime.datetime(2022,9,9,0)
flag = False

for table_name in table_name_list:
    cursor.execute(f"""
                   insert into {table_name} (now_time, value) VALUES ('2022-09-09 19:15:00', 0)
                """)
    con.commit()
    # value = randint(5,30) * 10
    # for i in [start+datetime.timedelta(minutes=x*10) for x in range(20)]: 
    #     cursor.execute(f"""
    #                 insert into {table_name} (now_time, value) VALUES ('{i}', {value})
    #                 """)
    #     con.commit()
    #     value += 30
    