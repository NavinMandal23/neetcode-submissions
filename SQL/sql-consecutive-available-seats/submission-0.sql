-- Write your query below
with cte as (
    select 
    seat_id, row_number() over(order by seat_id) rn
    from cinema
    where free = 1
),

base as 
(select seat_id, rn-seat_id, min(seat_id) over(partition by rn-seat_id )start_id, max(seat_id) over(partition by rn-seat_id) end_id
from cte 
)

select seat_id from base where start_id <> end_id order by seat_id