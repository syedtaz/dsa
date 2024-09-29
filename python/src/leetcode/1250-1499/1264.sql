with Friends as (
  select
    distinct user2_id as user_id
  from
    Friendship
  where
    user1_id = 1
  union
  select
    distinct user1_id as user_id
  from
    Friendship
  where
    user2_id = 1
)
select
  distinct L.page_id as recommended_page
from
  Likes L
  join Friends F on L.user_id = F.user_id
where
  L.page_id not in (
    select
      distinct page_id
    from
      Likes
    where
      user_id = 1
  )