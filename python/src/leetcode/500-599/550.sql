with Fst as (
  select
    player_id,
    min(event_date) as first_login
  from
    Activity
  group by
    player_id
)
select
  round(
    count(distinct A.player_id) :: numeric / (
      select
        count(distinct player_id) :: numeric
      from
        Activity
    ),
    2
  ) as fraction
from
  Activity A
  join Fst F on A.player_id = F.player_id
  and A.event_date = F.first_login + 1