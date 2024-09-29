with First as (
  select
    player_id,
    min(event_date) as first_login
  from
    Activity
  group by
    player_id
)
select
  Activity.player_id,
  Activity.device_id
from
  First
  join Activity on First.player_id = Activity.player_id
where
  First.first_login = Activity.event_date