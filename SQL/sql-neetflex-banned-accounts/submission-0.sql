-- Write your query below
with logs_dedup as (
    select distinct account_id, ip_address, login, logout
    from log_info
) 

select distinct l1.account_id
from logs_dedup l1 join logs_dedup l2 
on l1.account_id = l2.account_id and l1.ip_address <> l2.ip_address and 
l1.login between l2.login and l2.logout