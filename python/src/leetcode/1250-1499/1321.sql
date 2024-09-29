with Fst as (
  select
    min(visited_on) as earliest
  from
    Customer
),
Grouped as (
  select
    visited_on,
    sum(amount) as amount
  from
    Customer
  group by
    visited_on
),
Total as (
  select
    C.visited_on,
    sum(C.amount) over (
      order by
        C.visited_on rows between 6 preceding
        and current row
    ) as amount,
    round(
      avg(C.amount) over (
        order by
          C.visited_on rows between 6 preceding
          and current row
      ),
      2
    ) as average_amount
  from
    Grouped C
)
select
  *
from
  Total
where
  Total.visited_on - 6 >= (
    select
      *
    from
      Fst
  )
order by Total.visited_on