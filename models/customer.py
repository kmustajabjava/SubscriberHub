class Customer:

    def __init__(
        self,
        full_name,
        email,
        phone_number,
        city,
        registration_date,
        status,
        customer_id=None
    ):
        self.customer_id = customer_id
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.city = city
        self.registration_date = registration_date
        self.status = status

    def __str__(self):
        return (
            f"Customer("
            f"ID={self.customer_id}, "
            f"Name='{self.full_name}', "
            f"City='{self.city}', "
            f"Status='{self.status}')"
        )