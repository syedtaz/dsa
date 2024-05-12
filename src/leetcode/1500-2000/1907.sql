with Cat as (
  select
    *
  from
    (
      VALUES
        ('Low Salary'),
        ('High Salary'),
        ('Average Salary')
    ) as Cat(salary)
),
X as (
  select
    case
      when income < 20000 then 'Low Salary'
      when income > 50000 then 'High Salary'
      else 'Average Salary'
    end as salary
  from
    Accounts
),
Z as (
  select
    salary,
    count(salary)
  from
    X
  group by
    salary
)
select
  Cat.salary as category,
  coalesce(Z.count, 0) as accounts_count
from
  Cat
  left join Z on Cat.salary = Z.salary