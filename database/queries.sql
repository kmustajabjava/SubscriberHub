-- "We need a quick report showing all active customers, 
-- along with the plan they're currently subscribed to and the city they belong to. 
-- Sort the results alphabetically by customer name."

SELECT
    c.CustomerID,
    c.FullName,
    c.City,
    p.PlanName,
    s.Status
FROM Customers c
INNER JOIN Subscriptions s
    ON c.CustomerID = s.CustomerID
INNER JOIN Plans p
    ON s.PlanID = p.PlanID
WHERE c.Status = 'Active'
  AND s.Status = 'Active'
ORDER BY c.FullName;

-- whcih plan generated the most revenue
SELECT
    p.PlanName,
    SUM(pay.Amount) AS TotalRevenue
FROM Plans p

INNER JOIN Subscriptions s
    ON p.PlanID = s.PlanID

INNER JOIN Payments pay
    ON s.SubscriptionID = pay.SubscriptionID

WHERE pay.Status = 'Completed'

GROUP BY
    p.PlanID,
    p.PlanName

ORDER BY TotalRevenue DESC;