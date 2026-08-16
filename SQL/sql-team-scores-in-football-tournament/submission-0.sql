-- Write your query below
with cte as (
    select host_team, guest_team,
        h.team_name host, a.team_name guest, 
    case 
        when host_goals > guest_goals then 3 
        when host_goals = guest_goals then 1
        when host_goals < guest_goals then 0
    end as host_pts,
    case 
        when host_goals < guest_goals then 3 
        when host_goals = guest_goals then 1
        when host_goals > guest_goals then 0
    end as guest_pts
    from matches m 
    join teams h on m.host_team = h.team_id
    join teams a on m.guest_team = a.team_id
),

base as (
    select host_team team_id, host team_name, host_pts pts from cte
    union all 
    select guest_team team_id, guest team_name, guest_pts pts from cte
)

select coalesce(b.team_id, t.team_id) team_id,
    coalesce(b.team_name, t.team_name) team_name, 
    coalesce(sum(b.pts), 0) as num_points
from teams t 
left join base b on t.team_id = b.team_id
group by 1, 2
order by 3 desc, 1 asc