with Emp as (
  select
    employee_id,
    experience_years
  from
    Employee
)
select
  project_id,
  round(avg(experience_years), 2) as average_years
from
  (
    Project
    join Emp on Project.employee_id = Emp.employee_id
  )
group by
  project_id