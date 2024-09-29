select
  a.id,
  case
    when a.p_id is null
    and b.p_id is null then 'Root'
    when b.p_id is null then 'Inner'
    else 'Leaf'
  end as type
from
  Tree a
  left join Tree b on a.p_id = b.id