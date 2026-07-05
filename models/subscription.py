class Subscription:

    def __init__(
        self,
        customer_id,
        plan_id,
        start_date,
        end_date,
        status="Active",
        auto_renew=False,
        subscription_id=None
    ):
        self.subscription_id = subscription_id
        self.customer_id = customer_id
        self.plan_id = plan_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.auto_renew = auto_renew

    def __str__(self):
        return (
            f"Subscription("
            f"ID={self.subscription_id}, "
            f"Customer={self.customer_id}, "
            f"Plan={self.plan_id}, "
            f"Status='{self.status}')"
        )