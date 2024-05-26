select
  session_id
from
  Playback
  left join Ads on Ads.customer_id = Playback.customer_id
  and Ads.timestamp >= Playback.start_time
  and Ads.timestamp <= Playback.end_time
where
  ad_id is null