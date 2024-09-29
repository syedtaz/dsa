with Reviewers as (
  select
    user_id,
    count(*) as count
  from
    MovieRating
  group by
    user_id
  order by
    count desc
  fetch first
    1 rows with ties
),
Ratings as (
  select
    movie_id,
    avg(rating) as rating
  from
    MovieRating
  where
    extract(
      month
      from
        created_at
    ) = '02'
    and extract(
      year
      from
        created_at
    ) = '2020'
  group by
    movie_id
  order by
    rating desc
  fetch first
    1 rows with ties
) (
  select
    Users.name as results
  from
    Reviewers
    join Users on Reviewers.user_id = Users.user_id
  order by
    Users.name
  limit
    1
)
union
all (
  select
    Movies.title as results
  from
    Ratings
    join Movies on Ratings.movie_id = Movies.movie_id
  order by
    Movies.title
  limit
    1
)