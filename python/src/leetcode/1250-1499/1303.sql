with Sizes as (
  select
    team_id,
    count(employee_id) as team_size
  from
    Employee
  group by
    team_id
)
select
  Employee.employee_id,
  Sizes.team_size
from
  Employee
  join Sizes on Employee.team_id = Sizes.team_id