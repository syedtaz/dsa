with X as (
  select
    S.student_id,
    S.assignment1 + S.assignment2 + S.assignment3 as total
  from
    Scores S
)
select
  max(X.total) - min(X.total) as difference_in_score
from
  X