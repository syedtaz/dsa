select
  *
from
  Users
where
  split_part(mail, '@', 2) = 'leetcode.com'
  and split_part(mail, '@', 1) ~ '^[a-zA-Z]+([_a-zA-Z0-9.-]*)$'