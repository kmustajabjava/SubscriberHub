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


-- "How many customers do we have in each city? 
-- Show the cities with the highest number of customers first."
SELECT City, COUNT(CustomerID) AS totalCustomers 
FROM Customers
GROUP BY City
ORDER BY totalCustomers DESC;

-- "Show me every plan along with the number of customers currently subscribed to it. 
-- Include plans that currently have zero subscribers."
SELECT
    p.PlanID,
    p.PlanName,
    COUNT(s.CustomerID) AS TotalSubscribers
FROM Plans p

LEFT JOIN Subscriptions s
    ON p.PlanID = s.PlanID
    AND s.Status = 'Active'

GROUP BY
    p.PlanID,
    p.PlanName

ORDER BY
    TotalSubscribers DESC;


-- "Find all customers who have never opened a support ticket."
SELECT c.CustomerID ,c.FullName
FROM Customers c
LEFT JOIN SupportTickets s 
ON c.CustomerID = s.CustomerID
WHERE s.ticketID is Null;

-- "Find all plans that have never been subscribed to."
SELECT
    p.PlanID,
    p.PlanName
FROM Plans p

LEFT JOIN Subscriptions s
    ON p.PlanID = s.PlanID

WHERE s.SubscriptionID IS NULL; 


-- Show me the customers whose total completed payments are greater than 10,000 PKR.
SELECT
    c.CustomerID,
    c.FullName,
    SUM(p.Amount) AS TotalPaid
FROM Customers c

INNER JOIN Subscriptions s
    ON c.CustomerID = s.CustomerID

INNER JOIN Payments p
    ON s.SubscriptionID = p.SubscriptionID

WHERE p.Status = 'Completed'

GROUP BY
    c.CustomerID,
    c.FullName

HAVING SUM(p.Amount) > 10000

ORDER BY TotalPaid DESC;


-- Find all customers who have paid more than the average completed payment.
SELECT
    c.CustomerID,
    c.FullName,
    p.Amount
FROM Customers c

INNER JOIN Subscriptions s
    ON c.CustomerID = s.CustomerID

INNER JOIN Payments p
    ON s.SubscriptionID = p.SubscriptionID

WHERE
    p.Status = 'Completed'
    AND p.Amount >
    (
        SELECT AVG(Amount)
        FROM Payments
        WHERE Status = 'Completed'
    );


    -- Report showing every completed payment with the customer's name and plan name.
    SELECT *
FROM vw_CompletedPayments;