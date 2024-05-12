select
  project_id
from
  Project
group by
  project_id
order by
  count(distinct employee_id) desc
fetch first
  1 rows with ties