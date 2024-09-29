select
  next.id
from
  Weather next
  join Weather prev on (next.recorddate - prev.recorddate) = 1
where
  next.temperature > prev.temperature