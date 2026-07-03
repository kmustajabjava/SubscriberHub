
-- indexed columns that are frequently used in 
-- searches, 
-- joins, 
-- and reporting 
-- to improve query performance.
-- Customers

CREATE INDEX idx_customer_city
ON Customers(City);

CREATE INDEX idx_customer_status
ON Customers(Status);

-- Subscriptions

CREATE INDEX idx_subscription_customer
ON Subscriptions(CustomerID);

CREATE INDEX idx_subscription_plan
ON Subscriptions(PlanID);

CREATE INDEX idx_subscription_status
ON Subscriptions(Status);

-- Payments

CREATE INDEX idx_payment_status
ON Payments(Status);

CREATE INDEX idx_payment_date
ON Payments(PaymentDate);

-- Tickets

CREATE INDEX idx_ticket_status
ON SupportTickets(Status);

CREATE INDEX idx_ticket_priority
ON SupportTickets(Priority);