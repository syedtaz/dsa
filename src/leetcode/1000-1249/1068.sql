select
  P.product_name,
  S.year,
  S.price
from
  Sales S
join Product P on S.product_id = P.product_id