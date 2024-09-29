select
  W.name as warehouse_name,
  sum(P.width * P.length * P.height * W.units) as volume
from
  Warehouse W
  join Products P on W.product_id = P.product_id
group by
  warehouse_name