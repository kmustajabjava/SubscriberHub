class Payment:

    def __init__(
        self,
        subscription_id,
        amount,
        payment_method,
        payment_date,
        status="Pending",
        payment_id=None
    ):
        self.payment_id = payment_id
        self.subscription_id = subscription_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.status = status

    def __str__(self):
        return (
            f"Payment("
            f"ID={self.payment_id}, "
            f"Subscription={self.subscription_id}, "
            f"Amount=Rs.{self.amount}, "
            f"Status='{self.status}')"
        )