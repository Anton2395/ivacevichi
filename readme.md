время работы будет 1 или 0 (надо преобразовывать маску)
количество обработанных плит, деталей, облицовок - счётчик импульсов Целое число
скорость транспортёра 

with t as (
SELECT "key", now_time, value, coalesce(lag(value) OVER (order by now_time),3) as back_value
FROM public.mvlab_test_shkiper_skipper_status_work_mashine 
order by now_time
)
select now_time, value 
from t 
where value <> back_value