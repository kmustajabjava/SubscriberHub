USE SubscriberHub;

-- ==========================================
-- Customers
-- ==========================================

CREATE TABLE Customers (

    CustomerID INT AUTO_INCREMENT PRIMARY KEY,

    FullName VARCHAR(100) NOT NULL,

    Email VARCHAR(100) UNIQUE NOT NULL,

    PhoneNumber VARCHAR(15) UNIQUE NOT NULL,

    City VARCHAR(50) NOT NULL,

    RegistrationDate DATE NOT NULL DEFAULT (CURRENT_DATE),

    Status ENUM('Active','Inactive','Suspended')
    NOT NULL DEFAULT 'Active'

);

-- ==========================================
-- Plans
-- ==========================================

CREATE TABLE Plans (

    PlanID INT AUTO_INCREMENT PRIMARY KEY,

    PlanName VARCHAR(100) UNIQUE NOT NULL,

    SpeedMbps INT NOT NULL,

    Price DECIMAL(10,2) NOT NULL,

    DurationMonths INT NOT NULL,

    Status ENUM('Active','Inactive')
    NOT NULL DEFAULT 'Active'

);

-- ==========================================
-- Subscriptions
-- ==========================================

CREATE TABLE Subscriptions (

    SubscriptionID INT AUTO_INCREMENT PRIMARY KEY,

    CustomerID INT NOT NULL,

    PlanID INT NOT NULL,

    StartDate DATE NOT NULL,

    EndDate DATE NOT NULL,

    Status ENUM('Active','Expired','Cancelled','Paused')
    NOT NULL DEFAULT 'Active',

    AutoRenew BOOLEAN NOT NULL DEFAULT FALSE,

    CHECK (EndDate >= StartDate),

    FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID),

    FOREIGN KEY (PlanID)
        REFERENCES Plans(PlanID)

);

-- ==========================================
-- Payments
-- ==========================================

CREATE TABLE Payments (

    PaymentID INT AUTO_INCREMENT PRIMARY KEY,

    SubscriptionID INT NOT NULL,

    Amount DECIMAL(10,2) NOT NULL,

    PaymentDate DATE NOT NULL DEFAULT (CURRENT_DATE),

    PaymentMethod ENUM(
        'Cash',
        'Credit Card',
        'Debit Card',
        'Bank Transfer',
        'JazzCash',
        'EasyPaisa'
    ) NOT NULL,

    Status ENUM(
        'Pending',
        'Completed',
        'Failed',
        'Refunded'
    ) NOT NULL DEFAULT 'Pending',

    FOREIGN KEY (SubscriptionID)
        REFERENCES Subscriptions(SubscriptionID)

);

-- ==========================================
-- Support Tickets
-- ==========================================

CREATE TABLE SupportTickets (

    TicketID INT AUTO_INCREMENT PRIMARY KEY,

    CustomerID INT NOT NULL,

    IssueType ENUM(
        'Billing',
        'Technical',
        'Network',
        'General'
    ) NOT NULL,

    Description TEXT NOT NULL,

    Priority ENUM(
        'Low',
        'Medium',
        'High'
    ) NOT NULL DEFAULT 'Medium',

    Status ENUM(
        'Open',
        'In Progress',
        'Resolved',
        'Closed'
    ) NOT NULL DEFAULT 'Open',

    CreatedDate DATE NOT NULL DEFAULT (CURRENT_DATE),

    FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID)

);

-- ==========================================
-- Audit Logs
-- ==========================================

CREATE TABLE AuditLogs (

    LogID INT AUTO_INCREMENT PRIMARY KEY,

    CustomerID INT,

    ActionPerformed VARCHAR(255) NOT NULL,

    ActionDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID)

);