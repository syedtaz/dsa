select
  id,
  login_date,
  row_number() over(partition by id order by login_date)
from
  Logins