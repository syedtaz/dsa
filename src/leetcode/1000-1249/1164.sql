with Prices as (
  select
    distinct product_id,
    first_value (new_price) over (
      partition by product_id
      order by
        change_date desc
    ) as price
  from
    Products
  where
    change_date <= '2019-08-16'
),
Ids as (
  select
    distinct product_id
  from
    Products
)
select
  I.product_id,
  coalesce(P.price, 10) as price
from
  Ids I
  left join Prices P on I.product_id = P.product_id