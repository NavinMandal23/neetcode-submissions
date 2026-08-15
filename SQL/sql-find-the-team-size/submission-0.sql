-- Write your query below
with cte as 
(select team_id, count(employee_id) as cnt
from employee 
group by 1)

select employee_id, cnt as team_size
from cte join employee e on e.team_id = cte.team_id
