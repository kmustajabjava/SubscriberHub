from services.subscription_service import SubscriptionService


class SubscriptionController:

    def __init__(self):

        self.service = SubscriptionService()

    def create_subscription(self):

        print("\n===== CREATE SUBSCRIPTION =====\n")

        customer_id = int(input("Customer ID: "))
        plan_id = int(input("Plan ID: "))

        print("\nPayment Methods")
        print("1. Cash")
        print("2. Credit Card")
        print("3. Debit Card")
        print("4. Bank Transfer")
        print("5. JazzCash")
        print("6. EasyPaisa")

        payment_options = {
            "1": "Cash",
            "2": "Credit Card",
            "3": "Debit Card",
            "4": "Bank Transfer",
            "5": "JazzCash",
            "6": "EasyPaisa"
        }

        choice = input("\nSelect Payment Method: ")

        payment_method = payment_options.get(choice)

        if payment_method is None:
            print("Invalid payment method.")
            return

        auto_renew = input("Auto Renew (Y/N): ").strip().upper()

        auto_renew = auto_renew == "Y"

        success, message = self.service.create_subscription(
            customer_id,
            plan_id,
            payment_method,
            auto_renew
        )

        print(f"\n{message}")