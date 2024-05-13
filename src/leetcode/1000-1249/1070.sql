with Fst as (
  select
    product_id,
    min(year) as first_year
  from
    Sales
  group by
    product_id
)
select
  F.product_id,
  F.first_year,
  S.quantity,
  S.price
from
  Sales S
  join Fst F on S.product_id = F.product_id
  and S.year = F.first_year