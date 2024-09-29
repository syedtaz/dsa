with X as (
  select
    person_name,
    sum(weight) over (
      order by
        turn
    ) as sum
  from
    Queue
)
select
  person_name
from
  X
  join (
    select
      max(sum)
    from
      X
    where
      X.sum <= 1000
  ) Y on X.sum = Y.max