with Combined as (
  select
    Customers.customer_id,
    Customers.customer_name,
    Orders.product_name
  from
    Customers
    join Orders on Customers.customer_id = Orders.customer_id
),
Filtered as (
  select
    customer_id,
    string_agg(distinct product_name, ', ') as agg
  from
    Combined
  group by
    customer_id
)
select
  distinct Combined.customer_id,
  Combined.customer_name
from
  Combined
  inner join Filtered on Combined.customer_id = Filtered.customer_id
where
  agg not like '%C%'
  and agg like '%A, B%'