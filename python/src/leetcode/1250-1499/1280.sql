with Scores as (
  select
    student_id,
    subject_name,
    count(subject_name) as attended_exams
  from
    Examinations
  group by
    (student_id, subject_name)
)
select
  Students.student_id,
  Students.student_name,
  Subjects.subject_name,
  coalesce(Scores.attended_exams, 0) as attended_exams
from
  Students
  cross join Subjects
  left join Scores on Students.student_id = Scores.student_id
  and Subjects.subject_name = Scores.subject_name
order by
  Students.student_id,
  Subjects.subject_name