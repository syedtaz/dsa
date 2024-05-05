select
  name as Customers
from
  Customers
where
  id not in (
    select
      customerId as id
    from
      Orders
  )