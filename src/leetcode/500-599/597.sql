select
  *
from
  round(
    coalesce(
      (
        select
          count(*)
        from
          (
            select
              distinct requester_id,
              accepter_id
            from
              RequestAccepted
          )
      ) :: numeric / nullif(
        (
          select
            count(*)
          from
            (
              select
                distinct sender_id,
                send_to_id
              from
                FriendRequest
            )
        ) :: numeric,
        0
      ),
      0
    ),
    2
  ) as accept_rate