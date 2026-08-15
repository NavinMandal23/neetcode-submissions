-- Write your query below
SELECT name, sum(amount) balance
FROM users u JOIN transactions t ON u.account = t.account
GROUP BY name
HAVING sum(amount) > 10000