with Posts as (
  select
    distinct sub_id
  from
    Submissions
  where
    parent_id is null
),
Comb as (
  select
    count(distinct Submissions.sub_id),
    Submissions.parent_id
  from
    (
      Submissions
      join Posts on Submissions.parent_id = Posts.sub_id
    )
  group by
    parent_id
)
select
  sub_id as post_id,
  coalesce(count, 0) as number_of_comments
from
  (
    Posts
    left join Comb on Comb.parent_id = Posts.sub_id
  )