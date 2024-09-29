with X as (
  select
    A.employee_id as fst,
    B.employee_id as snd,
    C.employee_id as thd,
    D.employee_id as fth
  from
    Employees A
    left join Employees B on A.manager_id = B.employee_id
    left join Employees C on B.manager_id = C.employee_id
    left join Employees D on C.manager_id = D.employee_id
)
select
  fst as employee_id
from
  X
where
  (snd = 1 or thd = 1 or fth = 1) and fst != 1