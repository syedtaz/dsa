with Rates as (
  select
    company_id,
    case
      when max(salary) < 1000 then 0.0
      when max(salary) > 10000 then 0.49
      else 0.24
    end as rate
  from
    Salaries
  group by
    company_id
)
select
  S.company_id,
  S.employee_id,
  S.employee_name,
  round(S.salary - (S.salary * R.rate), 0) as salary
from
  Salaries S
  join Rates R on S.company_id = R.company_id