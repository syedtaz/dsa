select
  seller_id
from
  Sales
group by seller_id
order by sum(price) desc
fetch next 1 rows with ties
