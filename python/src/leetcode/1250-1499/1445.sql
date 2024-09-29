with A as (select sale_date, sold_num from Sales where fruit = 'apples'),
O as (select sale_date, sold_num from Sales where fruit = 'oranges')
select A.sale_date, (coalesce(A.sold_num - O.sold_num, A.sold_num)) as diff
from (A left join O on A.sale_date = O.sale_date)