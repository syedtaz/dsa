select
  actor_id,
  director_id
from
  (
    select
      actor_id,
      director_id,
      count(*)
    from
      ActorDirector
    group by
      actor_id,
      director_id
  ) A
where
  A.count >= 3