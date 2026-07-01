USE SubscriberHub;

-- =====================================================
-- SAMPLE DATA
-- =====================================================

-- =====================================================
-- PLANS
-- =====================================================

INSERT INTO Plans
(PlanName, SpeedMbps, Price, DurationMonths, Status)
VALUES
('Bronze',20,2500.00,1,'Active'),
('Silver',50,4000.00,1,'Active'),
('Gold',100,6500.00,1,'Active'),
('Platinum',200,9500.00,1,'Active'),
('Business Fiber',500,18000.00,1,'Active');



-- =====================================================
-- CUSTOMERS
-- =====================================================

INSERT INTO Customers
(
FullName,
Email,
PhoneNumber,
City,
RegistrationDate,
Status
)

VALUES

('Ali Raza','ali@email.com','03112223333','Islamabad','2026-01-02','Active'),

('Sara Khan','sara@email.com','03113334444','Rawalpindi','2026-01-05','Active'),

('Ahmed Ali','ahmed@email.com','03114445555','Lahore','2026-01-10','Active'),

('Fatima Zahra','fatima@email.com','03115556666','Islamabad','2026-02-01','Active'),

('Bilal Ahmed','bilal@email.com','03116667777','Faisalabad','2026-02-10','Active'),

('Usman Tariq','usman@email.com','03117778888','Peshawar','2026-02-18','Inactive'),

('Maryam Iqbal','maryam@email.com','03118889999','Karachi','2026-03-01','Active'),

('Hamza Khan','hamza@email.com','03119990000','Sialkot','2026-03-05','Suspended'),

('Ayesha Noor','ayesha@email.com','03001112222','Multan','2026-03-12','Active'),

('Hina Aslam','hina@email.com','03002223333','Gujranwala','2026-03-15','Active');

-- =====================================================
-- SUBSCRIPTIONS
-- =====================================================

INSERT INTO Subscriptions
(
    CustomerID,
    PlanID,
    StartDate,
    EndDate,
    Status,
    AutoRenew
)
VALUES

-- ===========================================
-- Customer 1 : Ali Raza
-- Gold → Gold Renewal → Platinum Upgrade
-- ===========================================

(1,3,'2026-01-02','2026-02-01','Expired',FALSE),

(1,3,'2026-02-02','2026-03-01','Expired',FALSE),

(1,4,'2026-03-02','2026-04-01','Active',TRUE),

-- ===========================================
-- Customer 2 : Sara Khan
-- Silver → Cancelled → Gold
-- ===========================================

(2,2,'2026-01-05','2026-02-04','Cancelled',FALSE),

(2,3,'2026-02-10','2026-03-09','Active',TRUE),

-- ===========================================
-- Customer 3 : Ahmed Ali
-- Bronze
-- ===========================================

(3,1,'2026-01-10','2026-02-09','Active',FALSE),

-- ===========================================
-- Customer 4 : Fatima Zahra
-- Business Fiber Renewal
-- ===========================================

(4,5,'2026-02-01','2026-03-02','Expired',TRUE),

(4,5,'2026-03-03','2026-04-02','Active',TRUE),

-- ===========================================
-- Customer 5 : Bilal Ahmed
-- Platinum → Business Fiber
-- ===========================================

(5,4,'2026-02-10','2026-03-09','Expired',FALSE),

(5,5,'2026-03-10','2026-04-09','Active',TRUE),

-- ===========================================
-- Customer 6 : Usman Tariq
-- Expired
-- ===========================================

(6,2,'2026-02-18','2026-03-17','Expired',FALSE),

-- ===========================================
-- Customer 7 : Maryam Iqbal
-- Gold
-- ===========================================

(7,3,'2026-03-01','2026-03-31','Active',TRUE),

-- ===========================================
-- Customer 8 : Hamza Khan
-- Suspended Customer
-- ===========================================

(8,1,'2026-03-05','2026-04-04','Paused',FALSE),

-- ===========================================
-- Customer 9 : Ayesha Noor
-- Business Fiber
-- ===========================================

(9,5,'2026-03-12','2026-04-11','Active',TRUE),

-- ===========================================
-- Customer 10 : Hina Aslam
-- Silver
-- ===========================================

(10,2,'2026-03-15','2026-04-14','Active',FALSE);


-- =====================================================
-- PAYMENTS
-- =====================================================

INSERT INTO Payments
(
    SubscriptionID,
    Amount,
    PaymentDate,
    PaymentMethod,
    Status
)
VALUES

-- =====================================================
-- Subscription 1
-- =====================================================
(1,6500.00,'2026-01-02','JazzCash','Completed'),

-- Subscription 2
(2,6500.00,'2026-02-02','EasyPaisa','Completed'),

-- Subscription 3
(3,9500.00,'2026-03-02','Bank Transfer','Completed'),

-- Subscription 4
(4,4000.00,'2026-01-05','Credit Card','Refunded'),

-- Subscription 5
(5,6500.00,'2026-02-10','JazzCash','Completed'),

-- Subscription 6
(6,2500.00,'2026-01-10','Cash','Completed'),

-- Subscription 7
(7,18000.00,'2026-02-01','Bank Transfer','Completed'),

-- Subscription 8
(8,18000.00,'2026-03-03','Bank Transfer','Completed'),

-- Subscription 9
(9,9500.00,'2026-02-10','Debit Card','Completed'),

-- Subscription 10
(10,18000.00,'2026-03-10','Bank Transfer','Completed'),

-- Subscription 11
(11,4000.00,'2026-02-18','EasyPaisa','Completed'),

-- Subscription 12
(12,6500.00,'2026-03-01','JazzCash','Completed'),

-- Subscription 13
(13,2500.00,'2026-03-05','Cash','Pending'),

-- Subscription 13 Retry
(13,2500.00,'2026-03-06','JazzCash','Completed'),

-- Subscription 14
(14,18000.00,'2026-03-12','Bank Transfer','Completed'),

-- Subscription 15
(15,4000.00,'2026-03-15','Credit Card','Completed'),


(3,9500.00,'2026-04-02','Bank Transfer','Completed'),

(5,6500.00,'2026-03-10','JazzCash','Completed'),

(8,18000.00,'2026-04-03','Bank Transfer','Completed'),

(10,18000.00,'2026-04-10','Bank Transfer','Completed'),

(12,6500.00,'2026-04-01','JazzCash','Completed'),

(14,18000.00,'2026-04-12','Bank Transfer','Completed'),

(15,4000.00,'2026-04-15','EasyPaisa','Completed'),

(3,9500.00,'2026-05-02','Bank Transfer','Completed'),

(5,6500.00,'2026-04-10','JazzCash','Completed'),

(8,18000.00,'2026-05-03','Bank Transfer','Completed'),

(10,18000.00,'2026-05-10','Bank Transfer','Pending'),

(10,18000.00,'2026-05-11','Bank Transfer','Completed'),

(14,18000.00,'2026-05-12','Bank Transfer','Completed'),

(12,6500.00,'2026-05-01','JazzCash','Completed');

-- SUPPORT TICKET

INSERT INTO SupportTickets
(
    CustomerID,
    IssueType,
    Description,
    Priority,
    Status
)
VALUES

(1,'Technical',
'Internet speed is much slower than subscribed package.',
'High',
'Resolved'),

(2,'Billing',
'Refund not received after cancellation.',
'Medium',
'Closed'),

(3,'Network',
'Internet is completely down since morning.',
'High',
'In Progress'),

(4,'Technical',
'Need assistance configuring static IP.',
'Low',
'Resolved'),

(5,'General',
'Customer requested upgrade to Business Fiber package.',
'Medium',
'Closed'),

(7,'Technical',
'Frequent WiFi disconnections.',
'Medium',
'Open'),

(8,'Billing',
'Payment marked failed although deducted.',
'High',
'Open'),

(9,'Network',
'High packet loss during office hours.',
'High',
'In Progress'),

(10,'General',
'Need router setup assistance.',
'Low',
'Closed'),

(1,'Technical',
'Router restarting automatically.',
'Medium',
'Open');

-- =====================================================
-- AUDIT LOGS
-- =====================================================

INSERT INTO AuditLogs
(
    CustomerID,
    SubscriptionID,
    ActionPerformed
)
VALUES

(1,1,'Customer Registered'),

(1,1,'Subscription Created'),

(1,2,'Subscription Renewed'),

(1,3,'Plan Upgraded to Platinum'),

(2,4,'Subscription Created'),

(2,4,'Subscription Cancelled'),

(2,5,'Gold Plan Purchased'),

(3,6,'Customer Registered'),

(3,6,'Payment Received'),

(4,7,'Business Fiber Activated'),

(4,8,'Subscription Renewed'),

(5,9,'Subscription Created'),

(5,10,'Plan Upgraded to Business Fiber'),

(5,10,'Payment Received'),

(6,11,'Subscription Expired'),

(7,12,'Customer Registered'),

(7,12,'Auto Renewal Enabled'),

(8,13,'Account Suspended'),

(8,13,'Payment Failed'),

(9,14,'Business Fiber Activated'),

(9,14,'Payment Received'),

(10,15,'Customer Registered'),

(10,15,'Silver Plan Activated'),

(10,15,'Payment Received'),

(1,3,'Support Ticket Created');