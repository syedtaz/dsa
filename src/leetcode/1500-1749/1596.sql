with X as (
  select
    customer_id,
    product_id,
    count(*) as count
  from
    Orders
  group by
    customer_id,
    product_id
),
Maxes as (
  select
    customer_id,
    max(count) as mcount
  from
    X
  group by
    customer_id
)
select
  X.customer_id,
  X.product_id,
  P.product_name
from
  X
  join Maxes M on M.customer_id = X.customer_id
  join Products P on X.product_id = P.product_id
where
  X.count = M.mcount