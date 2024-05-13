select
  count(
    case
      when extract(dow from submit_date) in (0, 6) then 1
    end
  ) as weekend_cnt,
  count(
    case
      when extract(dow from submit_date) not in (0, 6) then 1
    end
  ) as working_cnt
from
  Tasks