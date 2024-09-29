with X as (
  select
    country_id,
    (
      case
        when avg(weather_state) <= 15 then 'Cold'
        when avg(weather_state) >= 25 then 'Hot'
        else 'Warm'
      end
    ) as weather_type
  from
    Weather
  where
    extract(
      month
      from
        day
    ) = 11
    and extract(
      year
      from
        day
    ) = 2019
  group by
    country_id
)
select
  Countries.country_name,
  X.weather_type
from
  X
  join Countries on X.country_id = Countries.country_id