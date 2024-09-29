with Combined as (
  select
    Project.project_id,
    Employee.employee_id,
    Employee.experience_years
  from
    Project
    join Employee on Project.employee_id = Employee.employee_id
),
Maximum as (
  select
    Combined.project_id,
    max(Combined.experience_years)
  from
    Combined
  group by
    Combined.project_id
)
select
  Combined.project_id,
  Combined.employee_id
from
  Combined
  join Maximum on Combined.project_id = Maximum.project_id
where
  experience_years = max