with Counts as (
  select
    email,
    count(id)
  from
    Person
  group by
    email
)
select
  email
from
  Counts
where
  count > 1