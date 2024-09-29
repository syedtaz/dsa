select
  round(count(*) :: numeric * 100.0 / (
    select
      count(*)
    from
      Delivery
  ) :: numeric, 2) as immediate_percentage
from
  Delivery
where
  order_date = customer_pref_delivery_date