-- Write your query below
with cte as (
    select d.name as department, e.name as employee, e.salary, rank() over(partition by d.name order by e.salary desc) as rnk
from employee e join department d on e.department_id = d.id
)

select department, employee, salary
from cte 
where rnk = 1