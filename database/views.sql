CREATE VIEW vw_CompletedPayments AS

SELECT

    c.CustomerID,

    c.FullName,

    pl.PlanName,

    pay.PaymentID,

    pay.Amount,

    pay.PaymentDate,

    pay.PaymentMethod

FROM Customers c

INNER JOIN Subscriptions s
ON c.CustomerID = s.CustomerID

INNER JOIN Plans pl
ON s.PlanID = pl.PlanID

INNER JOIN Payments pay
ON s.SubscriptionID = pay.SubscriptionID

WHERE pay.Status='Completed';

---------------------------------------------------------------------------------------
-- Active Customers
CREATE VIEW vw_ActiveCustomers AS

SELECT

    c.CustomerID,
    c.FullName,
    c.Email,
    c.City,

    p.PlanName,

    s.StartDate,
    s.EndDate

FROM Customers c

INNER JOIN Subscriptions s
ON c.CustomerID = s.CustomerID

INNER JOIN Plans p
ON s.PlanID = p.PlanID

WHERE s.Status='Active';

-- ---------------------------------------------------------------------------------------
-- Pending Payments
CREATE VIEW vw_PendingPayments AS

SELECT

    pay.PaymentID,

    c.FullName,

    p.PlanName,

    pay.Amount,

    pay.PaymentDate

FROM Payments pay

INNER JOIN Subscriptions s
ON pay.SubscriptionID=s.SubscriptionID

INNER JOIN Customers c
ON s.CustomerID=c.CustomerID

INNER JOIN Plans p
ON s.PlanID=p.PlanID

WHERE pay.Status='Pending';

-- --------------------------------------------------------------------------
-- Customer Subscription History
CREATE VIEW vw_SubscriptionHistory AS

SELECT

    c.CustomerID,

    c.FullName,

    p.PlanName,

    s.Status,

    s.StartDate,

    s.EndDate

FROM Customers c

INNER JOIN Subscriptions s
ON c.CustomerID=s.CustomerID

INNER JOIN Plans p
ON s.PlanID=p.PlanID;

-- --------------------------------------------------------------------------------------------
-- Revenue By Plan
CREATE VIEW vw_RevenueByPlan AS

SELECT

    p.PlanName,

    SUM(pay.Amount) AS Revenue

FROM Plans p

INNER JOIN Subscriptions s
ON p.PlanID=s.PlanID

INNER JOIN Payments pay
ON s.SubscriptionID=pay.SubscriptionID

WHERE pay.Status='Completed'

GROUP BY p.PlanName;