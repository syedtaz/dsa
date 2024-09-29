with Combined as (
  select
    Department.name as Department,
    Employee.name as Employee,
    Employee.salary as Salary
  from
    Employee
    join Department on employee.departmentid = department.id
)
select
  Combined.department,
  Combined.employee,
  Combined.salary
from
  (
    Combined
    join (
      select
        department,
        max(salary)
      from
        Combined
      group by
        Department
    ) Filtered on Combined.department = Filtered.department
  )
where
  Combined.salary = Filtered.max