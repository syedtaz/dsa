select
  P.product_id,
  P.product_name from (
    select
      distinct S.product_id
    from
      Sales S
    group by
      S.product_id
    having
      min(S.sale_date) >= '2019-01-01' :: date
      and max(S.sale_date) <= '2019-03-31' :: date
  ) X
  join Product P on X.product_id = P.product_id