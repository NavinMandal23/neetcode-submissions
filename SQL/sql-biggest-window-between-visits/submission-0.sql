with cte as (
    select user_id, visit_date, lead(visit_date, 1, '2021-01-01'::DATE) over(partition by user_id order by visit_date) next_visit_date
    from user_visits
)
select 
user_id, 
max(next_visit_date - visit_date) as biggest_window
from cte
group by 1
order by 1