with Debit as (
  select
    paid_to as user_id,
    sum(amount) as amount
  from
    Transactions
  group by
    paid_to
),
Credit as (
  select
    paid_by as user_id,
    sum(amount) as amount
  from
    Transactions
  group by
    paid_by
)
select
  U.user_id,
  U.user_name,
  U.credit + coalesce(D.amount, 0) - coalesce(C.amount, 0) as credit,
  case
    when U.credit + coalesce(D.amount, 0) - coalesce(C.amount, 0) <= 0 then 'Yes'
    else 'No'
  end as credit_limit_breached
from
  Users U
  left join Debit D on U.user_id = D.user_id
  left join Credit C on U.user_id = C.user_id