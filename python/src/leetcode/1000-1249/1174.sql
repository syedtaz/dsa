with Y as (
  select
    order_date,
    customer_pref_delivery_date
  from
    (
      select
        customer_id,
        min(order_date) as first_order
      from
        Delivery
      group by
        customer_id
    ) X
    join Delivery D on X.customer_id = D.customer_id
    and X.first_order = D.order_date
)
select
  round(count(*) :: numeric  * 100.0 / (
    select
      count(*)
    from
      Y
  ) :: numeric, 2) as immediate_percentage
from
  Y
where
  Y.order_date = Y.customer_pref_delivery_date