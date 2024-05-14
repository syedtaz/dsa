with Pairs as (
  select
    user1_id as a,
    user2_id as b
  from
    Friendship
  union
  all
  select
    user2_id as a,
    user1_id as b
  from
    Friendship
),
Common as (
  select
    A.a as user1_id,
    B.a as user2_id,
    count(*) as common_friend
  from
    Pairs A
    join Pairs B on A.b = B.b
  where
    A.a < B.a
  group by
    A.a,
    B.a
  having
    count(*) >= 3
)
select
  C.user1_id,
  C.user2_id,
  C.common_friend
from
  Common C
  join Friendship F
  on F.user1_id = C.user1_id and F.user2_id = C.user2_id