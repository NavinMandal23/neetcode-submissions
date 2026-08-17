-- Write your query below
with ranked as (
    select p.project_id, e.employee_id, rank() over(partition by p.project_id order by e.experience_years desc) rnk 
    from employee e join project p on e.employee_id = p.employee_id
)
select 
project_id, employee_id
from ranked
where rnk = 1