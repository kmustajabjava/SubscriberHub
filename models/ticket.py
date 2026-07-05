class SupportTicket:

    def __init__(
        self,
        customer_id,
        issue_type,
        description,
        priority,
        created_date,
        status="Open",
        ticket_id=None
    ):

        self.ticket_id = ticket_id
        self.customer_id = customer_id
        self.issue_type = issue_type
        self.description = description
        self.priority = priority
        self.status = status
        self.created_date = created_date

    def __str__(self):

        return (
            f"Ticket("
            f"ID={self.ticket_id}, "
            f"Customer={self.customer_id}, "
            f"Issue='{self.issue_type}', "
            f"Priority='{self.priority}', "
            f"Status='{self.status}')"
        )