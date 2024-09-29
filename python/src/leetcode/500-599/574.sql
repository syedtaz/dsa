select
  C.name from (
    select
      candidateid,
      count(*) as votes
    from
      Vote
    group by
      candidateid
    order by
      votes desc
    limit
      1
  ) V
  join Candidate C on V.candidateid = C.id