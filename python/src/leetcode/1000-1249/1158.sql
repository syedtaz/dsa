select
  U.user_id as buyer_id,
  U.join_date,
  coalesce(X.orders_in_2019, 0) as orders_in_2019
from
  Users U
  left join (
    select
      buyer_id,
      count(*) as orders_in_2019
    from
      Orders
    where
      extract(
        year
        from
          order_date
      ) = '2019'
    group by
      buyer_id
  ) X on X.buyer_id = U.user_id