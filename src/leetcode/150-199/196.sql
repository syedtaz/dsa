delete from
  Person
where
  id in (
    select
      id
    from
      Person
    except
      (
        select
          min(Person.id) as id
        from
          Person
        group by
          Person.email
      )
  )