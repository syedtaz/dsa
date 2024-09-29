select
  S.score,
  dense_rank() over (
    order by
      S.score desc
  ) as rank
from
  Scores S