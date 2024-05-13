with Rank as (
  select
    *,
    dense_rank() over (
      partition by day
      order by
        amount desc
    ) as rank
  from
    Transactions
)
select
  transaction_id
from
  Rank
where
  rank = 1
  order by transaction_id