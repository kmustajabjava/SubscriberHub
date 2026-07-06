# SubscriberHub Functional Requirements

## Overview

SubscriberHub is a console-based Customer Subscription Management System designed for a telecom environment. The application manages customers, subscription plans, payments, support tickets, and audit logs using a MySQL relational database.

---

# Customer Management

## Register Customer

Purpose:
Create a new customer record.

Process:

1. User enters customer information.
2. Input is validated.
3. Email and phone uniqueness are verified.
4. INSERT statement stores customer in MySQL.
5. Audit log is created.

Database Operations

- INSERT Customers
- INSERT AuditLogs

---

## Display Customers

Purpose:

Display all registered customers.

Process

1. Retrieve all customer records.
2. Convert database rows into Customer objects.
3. Display results.

Database Operations

- SELECT Customers

---

## Search Customer

Supports searching by:

- Customer ID
- Name
- Email
- Phone Number

Database Operations

- SELECT Customers

---

# Subscription Management

## Create Subscription

Purpose

Assign a subscription plan to a customer.

Process

1. Verify customer exists.
2. Verify plan exists.
3. Expire previous active subscription.
4. Create new subscription.
5. Generate payment record.
6. Create audit log.

Database Operations

- UPDATE Subscriptions
- INSERT Subscriptions
- INSERT Payments
- INSERT AuditLogs

---

## View Subscriptions

Displays all subscriptions.

Database Operations

- SELECT with INNER JOIN

---

## Search Subscription

Search subscription using Subscription ID.

Database Operations

- SELECT with INNER JOIN

---

## Pause Subscription

Changes subscription status from Active to Paused.

Database Operations

- UPDATE Subscriptions

---

## Resume Subscription

Changes status from Paused to Active.

Database Operations

- UPDATE Subscriptions

---

## Cancel Subscription

Changes status to Cancelled.

Database Operations

- UPDATE Subscriptions

---

# Payment Management

## View Payments

Displays payment history with customer and plan details.

Database Operations

- SELECT with INNER JOIN

---

## Search Payment

Retrieves payment by Payment ID.

Database Operations

- SELECT

---

## Complete Payment

Updates payment status to Completed.

Database Operations

- UPDATE Payments

---

## Fail Payment

Updates payment status to Failed.

Database Operations

- UPDATE Payments

---

## Refund Payment

Updates payment status to Refunded.

Database Operations

- UPDATE Payments

---

# Support Ticket Management

## Create Ticket

Creates a support request for a customer.

Database Operations

- INSERT SupportTickets

---

## View Tickets

Displays all support tickets.

Database Operations

- SELECT with INNER JOIN

---

## Search Ticket

Searches using Ticket ID.

Database Operations

- SELECT

---

## Update Ticket Status

Changes ticket status.

Database Operations

- UPDATE SupportTickets

---

## Close Ticket

Marks ticket as Closed.

Database Operations

- UPDATE SupportTickets

---

# Audit Logging

Audit logs record important business events.

Currently logged events:

- Customer Registration
- Subscription Creation

Database Operations

- INSERT AuditLogs