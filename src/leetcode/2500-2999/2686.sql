with Total as (
  select
    order_date,
    count(*)
  from
    Delivery
  group by
    order_date
),
Uniq as (
  select
    order_date,
    count(*)
  from
    Delivery
  where
    order_date = customer_pref_delivery_date
  group by
    order_date
)

select
  Total.order_date,
  round(coalesce(Uniq.count, 0.0) :: numeric * 100.0 / Total.count :: numeric, 2) as immediate_percentage
from Total left join Uniq on Total.order_date = Uniq.order_date
order by Total.order_date