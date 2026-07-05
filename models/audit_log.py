class AuditLog:

    def __init__(
        self,
        customer_id,
        action_performed,
        action_date=None,
        log_id=None
    ):

        self.log_id = log_id
        self.customer_id = customer_id
        self.action_performed = action_performed
        self.action_date = action_date

    def __str__(self):

        return (
            f"AuditLog("
            f"ID={self.log_id}, "
            f"Customer={self.customer_id}, "
            f"Action='{self.action_performed}', "
            f"Date='{self.action_date}')"
        )