class Plan:

    def __init__(
        self,
        plan_name,
        speed,
        price,
        plan_id=None
    ):
        self.plan_id = plan_id
        self.plan_name = plan_name
        self.speed = speed
        self.price = price

    def __str__(self):
        return (
            f"Plan("
            f"ID={self.plan_id}, "
            f"Name='{self.plan_name}', "
            f"Speed='{self.speed}', "
            f"Price=Rs.{self.price})"
        )