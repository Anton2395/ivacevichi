import datetime
from pytz import timezone

from sqlalchemy.orm import Session

from Machine import models


tz = timezone('Europe/Minsk')


def get_param_machine_shift(
        db: Session,
        machine: models.Machine,
        date: datetime.date,
        shift: models.ShiftWorkshop,
        flag_now: bool = False
) -> dict:
    """
    Возвращает параметры машины в рамках заданной смены и заданного дня

    :param db: сущность соединения с базой
    :param machine: сущность машины
    :param date: дата за которую происходит сбор данных
    :param shift: сущность смены
    :param flag_now: флаг показывающий что сбор происходет текущей (ещё не законченной) смены
    """
    response = {}
    start = datetime.datetime.combine(date, shift.start)
    end = datetime.datetime.combine(date, shift.end)
    name_mashine = machine.name
    value_type = machine.type_mash.value
    response["name_mashine"] = name_mashine
    response["shift"] = shift.name
    if value_type == 1:
        name_area = "skipper"
        response["count_processed_parts"] = get_count_processed_part_shift(db=db, name=name_mashine,
                                                                           area_name=name_area, start=start, end=end)
    if value_type == 2:
        name_area = "ima_novimat_l20"
        response["count_facings"] = get_count_facings_shift(db=db, name=name_mashine, area_name=name_area,
                                                            start=start, end=end)
        response["conveyor_speed"] =  get_conveyor_speed_shift(db=db, name=name_mashine, area_name=name_area,
                                                               start=start, end=end)
    if value_type == 3:
        name_area = "ima_novimat_l12"
        response["count_facings"] = get_count_facings_shift(db=db, name=name_mashine, area_name=name_area, start=start,
                                                            end=end)
        response["conveyor_speed"] =  get_conveyor_speed_shift(db=db, name=name_mashine, area_name=name_area,
                                                               start=start, end=end)
    if value_type == 4:
        name_area = "ima_novimat_r3_plus"
        response["count_facings"] = get_count_facings_shift(db=db, name=name_mashine, area_name=name_area, start=start,
                                                            end=end)
        response["conveyor_speed"] =  get_conveyor_speed_shift(db=db, name=name_mashine, area_name=name_area,
                                                               start=start, end=end)
    if value_type == 5:
        name_area = "ima_novimat_r3"
        response["count_facings"] = get_count_facings_shift(db=db, name=name_mashine, area_name=name_area, start=start,
                                                            end=end)
        response["conveyor_speed"] =  get_conveyor_speed_shift(db=db, name=name_mashine, area_name=name_area,
                                                               start=start, end=end)
    if value_type == 6:
        name_area = "holzma_hpp"
        response["count_processed_boards"] = get_count_processed_boards_shift(db=db, name=name_mashine,
                                                                              area_name=name_area, start=start, end=end)
    if value_type == 7:
        name_area = "schelling_fh4"
        response["count_processed_boards"] = get_count_processed_boards_shift(db=db, name=name_mashine,
                                                                              area_name=name_area, start=start, end=end)
    if value_type == 8:
        name_area = "bima_410v"
        response["count_processed_parts"] = get_count_processed_part_shift(db=db, name=name_mashine,
                                                                           area_name=name_area, start=start, end=end)
    if value_type == 9:
        name_area = "rover_s1_30"
        response["count_processed_parts"] = get_count_processed_part_shift(db=db, name=name_mashine,
                                                                           area_name=name_area, start=start, end=end)
    if value_type == 10:
        name_area = "holzma_hkl11"
        response["count_processed_boards"] = get_count_processed_boards_shift(db=db, name=name_mashine,
                                                                              area_name=name_area, start=start, end=end)
    if value_type == 11:
        name_area = "unimak"
    if value_type == 12:
        name_area = "ima_combivis_l12"
        response["count_facings"] = get_count_facings_shift(db=db, name=name_mashine, area_name=name_area,
                                                            start=start, end=end)
        response["conveyor_speed"] =  get_conveyor_speed_shift(db=db, name=name_mashine, area_name=name_area,
                                                               start=start, end=end)
    if value_type == 13:
        name_area = "ima_combivis_r3"
        response["count_facings"] = get_count_facings_shift(db=db, name=name_mashine, area_name=name_area, start=start,
                                                            end=end)
        response["conveyor_speed"] =  get_conveyor_speed_shift(db=db, name=name_mashine, area_name=name_area,
                                                               start=start, end=end)
    if value_type == 14:
        name_area = "biesse_techno_ftd"
        response["count_processed_parts"] = get_count_processed_part_shift(db=db, name=name_mashine,
                                                                           area_name=name_area, start=start, end=end)
    if value_type == 15:
        name_area = "homag"
    if value_type == 16:
        name_area = "biesse_ftd_cn"
        response["count_processed_parts"] = get_count_processed_part_shift(db=db, name=name_mashine,
                                                                           area_name=name_area, start=start, end=end)
    response["duration_work"] = get_time_work_shift(db=db, name=name_mashine, area_name=name_area, start=start, end=end)
    response["duration_power"] = get_time_power_shift(db=db, name=name_mashine, area_name=name_area, start=start,
                                                      end=end)
    response["duration_bad"] = round(response["duration_power"] - response["duration_work"], 3)
    response["date"] = date.strftime("%d.%m.%Y")
    if flag_now:
        response['status_power'] = get_status_power_machine(db=db, name=name_mashine, area_name=name_area, start=start,
                                                            end=end)
        if machine.status_connect:
            response['status_connect'] = {
                "text": "Соединение установлено",
                "color": "#6FCF97"
            }
        else:
            response['status_connect'] = {
                "text": "Соединение не установлено",
                "color": "#EB5757"
            }
            response['status_power'] = False
    return response


def get_count_processed_boards_shift(
        db: Session,
        name: str,
        area_name: str,
        start: datetime.datetime,
        end: datetime.datetime
) -> int:
    """
    Возвращает количество обработанных плит

    :param db: сущность соединения с базой
    :param name: имя машины
    :param area_name: имя пространства данных
    :param start: начало смены
    :param end: конец смены
    """
    count_list = db.execute(f"""
                SELECT value
                    FROM mvlab_{name}_{area_name}_count_processed_boards
                        WHERE now_time > '{start}' and
                            now_time < '{end}'
                                ORDER BY now_time 
                """).all()
    if count_list:
        first = count_list[0][0]
        finish = count_list[-1][0]
        if finish < first:
            count = 4294967295 - first + finish + 1
        else:
            count = finish - first + 1

    else:
        count = 0
    return count


def get_conveyor_speed_shift(
        db: Session,
        name: str,
        area_name: str,
        start: datetime.datetime,
        end: datetime.datetime
) -> float:
    """
    Возвращает среднюю скорость конвеера

    :param db: сущность соединения с базой
    :param name: имя машины
    :param area_name: имя пространства данных
    :param start: начало смены
    :param end: конец смены
    """
    speed_list = db.execute(f"""
                select avg(value) from  (SELECT value
                    FROM mvlab_{name}_{area_name}_conveyor_speed
                        WHERE now_time > '{start}' and now_time < '{end}'
                ) as t
                """).first()
    return speed_list[0]


def get_count_facings_shift(
        db: Session,
        name: str,
        area_name: str,
        start: datetime.datetime,
        end: datetime.datetime
) -> int:
    """
    Возвращает количество облицовок

    :param db: сущность соединения с базой
    :param name: имя машины
    :param area_name: имя пространства данных
    :param start: начало смены
    :param end: конец смены
    """
    count_list = db.execute(f"""
                SELECT value
                    FROM mvlab_{name}_{area_name}_count_facings
                        WHERE now_time > '{start}' and
                            now_time < '{end}'
                                ORDER BY now_time
                """).all()
    if count_list:
        first = count_list[0][0]
        finish = count_list[-1][0]
        if finish < first:
            count = 4294967295 - first + finish + 1
        else:
            count = finish - first + 1
    else:
        count = 0
    return count


def get_count_processed_part_shift(
        db: Session,
        name: str,
        area_name: str,
        start: datetime.datetime,
        end: datetime.datetime
) -> int:
    """
    Возвращает количество обработанных деталей

    :param db: сущность соединения с базой
    :param name: имя машины
    :param area_name: имя пространства данных
    :param start: начало смены
    :param end: конец смены
    :return:  число деталей
    """
    count_list = db.execute(f"""
                SELECT value
                    FROM mvlab_{name}_{area_name}_count_processed_parts
                        WHERE now_time > '{start}' and
                                now_time < '{end}'
                                    ORDER BY now_time
                """).all()
    if count_list:
        first = count_list[0][0]
        finish = count_list[-1][0]
        if finish < first:
            count = 4294967295 - first + finish + 1
        else:
            count = finish - first + 1
    else:
        count = 0
    return count


def get_duration_from_list(start_duration: int, end, list_time) -> int:
    """
    Расчитывает продолжительность (в секундах) массива с временными параметрами работы машины (time, status)

    :param start_duration: начальное значение продолжительности в секундах
    :param end: конец временной рамки (смены)
    :param list_time:  массив временных параметров работы
    :return: продолжительность работы в секундах
    """
    duration = start_duration
    start_time = None
    for time, val in list_time:
        if val == 1:
            if not start_time:
                start_time = time
        else:
            if start_time:
                duration += (time-start_time).total_seconds()
                start_time = None
    if start_time:
        now = tz.localize(datetime.datetime.now())
        if start_time < now < end:
            duration += (now - start_time).total_seconds()
        else:
            duration += (end - start_time).total_seconds()
    return duration


def get_old_line(db: Session, start: datetime.datetime, table_name: str) -> tuple:
    """
    Возвращает последнюю запись предыдущей смены параметра машины

    :param db: сущность соединения с базой
    :param start: дата и время начало смены
    :param table_name: имя таблицы станка
    :return: последняя запись перед началом смены
    """
    return db.execute(f"""
                    SELECT now_time, value
                    FROM {table_name}
                    WHERE now_time < '{start}'
                    order by now_time desc
                    LIMIT 1
                              """).first()
    

def get_time_power_shift(
        db: Session,
        name: str,
        area_name: str,
        start: datetime.datetime,
        end: datetime.datetime
) -> float:
    """
    Подсчитывает продолжительность питания машины

    :param db: сущность соединения с базой
    :param name: имя машины
    :param area_name: имя пространства данных
    :param start: начало смены
    :param end: конец смены
    :return: продолжительность питания машины в часах
    """
    power_time_array = db.execute(f"""
                    SELECT now_time, value
                    FROM mvlab_{name}_{area_name}_status_power_mashine
                    WHERE now_time > '{start}' and
                        now_time < '{end}'
                    order by now_time
                """).all()
    duration_sec = 0
    if power_time_array:
        if power_time_array[0][1] == 0:
            duration_sec += (power_time_array[0][0] - tz.localize(start)).total_seconds()
        duration_sec = get_duration_from_list(
            start_duration=duration_sec,
            end=tz.localize(end),
            list_time=power_time_array
        )
    else:
        old_line = get_old_line(
            db=db,
            start=start,
            table_name=f'mvlab_{name}_{area_name}_status_power_mashine'
        )
        if old_line:
            if old_line[1] == 1:
                now = tz.localize(datetime.datetime.now())
                if tz.localize(start) < now < tz.localize(end):
                    duration_sec += (now - tz.localize(start)).total_seconds()
                else:
                    duration_sec += (tz.localize(end) - tz.localize(start)).total_seconds()
    return round(duration_sec/3600, 3)


def get_status_power_machine(
        db: Session,
        name: str,
        area_name: str,
        start: datetime.datetime,
        end: datetime.datetime
) -> bool:
    """
    Проверяет статус питания машины

    :param db: сущность соединения с базой
    :param name: имя машины
    :param area_name: имя пространства данных
    :param start: начало смены
    :param end: конец смены
    :return: статус питания машины
    """
    power_time = db.execute(f"""
                SELECT now_time, value
                    FROM mvlab_{name}_{area_name}_status_power_mashine
                    WHERE now_time > '{start}' and
                        now_time < '{end}'
                    order by now_time
                """).first()
    if power_time:
        if power_time[1]:
            return True
    else:
        old_line = get_old_line(
            db=db,
            start=start,
            table_name=f'mvlab_{name}_{area_name}_status_power_mashine'
        )
        if old_line:
            if old_line[1]:
                return True
    return False


def get_time_work_shift(
        db: Session,
        name: str,
        area_name: str,
        start: datetime.datetime,
        end: datetime.datetime
) -> float:
    """
    Подсчитывает продолжительность работы машины

    :param db: сущность соединения с базой
    :param name: имя машины
    :param area_name: имя пространства данных
    :param start: начало смены
    :param end: конец смены
    :return: продолжительность работы машины в часах
    """
    work_time_array = db.execute(f"""
                SELECT now_time, value
                FROM mvlab_{name}_{area_name}_status_work_mashine
                WHERE now_time > '{start}' and
                    now_time < '{end}'
                order by now_time
               """).all()
    duration_sec = 0
    if work_time_array:
        if work_time_array[0][1] == 0:
            duration_sec += (work_time_array[0][0] - tz.localize(start)).total_seconds()
        duration_sec = get_duration_from_list(
            start_duration=duration_sec,
            end=tz.localize(end),
            list_time=work_time_array
        )
    else:
        old_line = get_old_line(
            db=db,
            start=start,
            table_name=f'mvlab_{name}_{area_name}_status_power_mashine'
        )
        if old_line:
            if old_line[1] == 1:
                now = tz.localize(datetime.datetime.now())
                if tz.localize(start) < now < tz.localize(end):
                    duration_sec += (now - tz.localize(start)).total_seconds()
                else:
                    duration_sec += (tz.localize(end) - tz.localize(start)).total_seconds()
    return round(duration_sec/3600, 3)


def get_param_machine_day(db: Session, start_date: int, end_date: int) -> list:
    """
    Расчитывает параметры всех машин за указанный период

    :param db: сущность соединения с базой
    :param start_date: дата начала расчёта
    :param end_date: дата конца расчёта
    :return: лист с параметрами машин
    """
    start = datetime.datetime.fromtimestamp(start_date).date()
    end = datetime.datetime.fromtimestamp(end_date).date()
    machine_list = db.query(models.Machine).order_by(models.Machine.id.asc()).all()
    shift_list = db.query(models.ShiftWorkshop).order_by(models.ShiftWorkshop.id.asc()).all()
    response = []
    for date in [start+datetime.timedelta(days=x) for x in range((end-start).days+1)]:
        for machine in machine_list:
            for shift in shift_list:
                response.append(get_param_machine_shift(
                    db=db,
                    machine=machine,
                    date=date,
                    shift=shift
                ))
    return response


def get_param_machine_now(db: Session) -> list:
    """
    Расчитывает параметры всех машин текущей смены

    :param db: сущность соединения с базой
    :return: лист с параметрами машин текущей смены
    """
    shifts = db.query(models.ShiftWorkshop).order_by(models.ShiftWorkshop.id.asc()).all()
    all_machine = db.query(models.Machine).order_by(models.Machine.id.asc()).all()
    datetime_now = datetime.datetime.now()
    response = []
    for shift in shifts:
        if shift.start < datetime_now.time() < shift.end:
            for machine in all_machine:
                response.append(get_param_machine_shift(
                    db=db,
                    machine=machine,
                    date=datetime_now.date(),
                    shift=shift,
                    flag_now=True))
            break
    return response
