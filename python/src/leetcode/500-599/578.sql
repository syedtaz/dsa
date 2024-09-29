with Total as (
  select
    question_id,
    count(*)
  from
    SurveyLog
  where
    action = 'show'
    or action = 'skip'
  group by
    question_id
),
Answered as (
  select
    question_id,
    count(*)
  from
    SurveyLog
  where
    action = 'answer'
  group by
    question_id
)
select
  T.question_id as survey_log
from
  Total T
  left join Answered A on T.question_id = A.question_id
order by
  coalesce(A.count, 0) :: numeric / T.count :: numeric desc,
  T.question_id
limit
  1