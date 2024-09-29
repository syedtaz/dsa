select
  name
from
  SalesPerson
where
  sales_id not in (
    select
      distinct sales_id
    from
      Orders o
      join Company c on o.com_id = c.com_id
    where
      name like 'RED'
  )