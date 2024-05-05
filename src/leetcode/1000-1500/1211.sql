select
  query_name,
  round(avg(rating :: numeric / position), 2) as quality,
  round(
    sum((rating < 3) :: int) :: numeric / nullif(count(query_name), 0) * 100,
    2
  ) as poor_query_percentage
from
  Queries
where
  query_name is not null
group by
  query_name