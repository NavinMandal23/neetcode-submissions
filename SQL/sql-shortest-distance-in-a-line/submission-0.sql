-- Write your query below
with cte as (
    select 
    p1.x p1, p2.x p2, abs(p1.x - p2.x) as dist
    from point p1 cross join point p2
    
)

select min(dist) shortest from cte where p1 <> p2