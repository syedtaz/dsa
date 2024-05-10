select
  distinct buyer_id
from
  Sales
  join Product on Sales.product_id = Product.product_id
where
  product_name = 'S8'
  and buyer_id not in (
    select
      distinct buyer_id
    from
      Sales
      join Product on Sales.product_id = Product.product_id
    where
      product_name = 'iPhone'
  )