with Grades as (
  select
    student_id,
    max(grade) as grade
  from
    Enrollments
  group by
    student_id
)
select
  E.student_id,
  min(E.course_id) as course_id,
  E.grade
from
  Enrollments E
  join Grades G on E.student_id = G.student_id
  and E.grade = G.grade
group by
  E.student_id,
  E.grade
order by
  E.student_id