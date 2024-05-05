select
  class
from
  (
    select
      count(*),
      class
    from
      Courses
    group by
      class
  ) A
where
  A.count >= 5