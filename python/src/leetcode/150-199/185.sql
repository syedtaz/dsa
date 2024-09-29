with Ranks as (
  select
    *,
    rank() over (
      partition by departmentid
      order by
        salary desc
    ) as rank
  from
    Employee
)
select
  *
from
  Ranks
where
  rank <= 3