select
  Users.name,
  coalesce(A.sum, 0) as travelled_distance
from
  Users
  left join (
    select
      user_id,
      sum(distance)
    from
      Rides
    group by
      user_id
  ) A on A.user_id = Users.id
order by
  travelled_distance desc,
  name