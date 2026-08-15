-- Write your query below
with cte as (
    select 
        least(from_id, to_id) as p1,
        greatest(from_id, to_id) as p2,
        duration
    from calls
)

select p1 as person1, p2 as person2, count(1) as call_count, sum(duration) as total_duration
from cte
group by 1,2
