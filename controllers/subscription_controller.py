from services.subscription_service import SubscriptionService


class SubscriptionController:

    def __init__(self):

        self.service = SubscriptionService()

    def subscription_menu(self):

        while True:

            print("\n===== SUBSCRIPTION MANAGEMENT =====")

            print("1. Create Subscription")
            print("2. View All Subscriptions")
            print("3. Search Subscription")
            print("4. Pause Subscription")
            print("5. Resume Subscription")
            print("6. Cancel Subscription")
            print("0. Back")

            choice = input("\nSelect Option: ")

            if choice == "1":

                self.create_subscription()

            elif choice == "2":

                self.display_subscriptions()

            elif choice == "3":

                self.search_subscription()

            elif choice == "4":

                self.pause_subscription()

            elif choice == "5":

                self.resume_subscription()

            elif choice == "6":

                self.cancel_subscription()

            elif choice == "0":

                break

            else:

                print("Invalid option.")

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

    def display_subscriptions(self):

        subscriptions = self.service.get_all_subscriptions()

        print("\n========== SUBSCRIPTIONS ==========\n")

        if not subscriptions:

            print("No subscriptions found.")
            return

        for sub in subscriptions:

            self.print_subscription(sub)
            print("-" * 50)


    def print_subscription(self, sub):

        print(f"\nSubscription ID : {sub['SubscriptionID']}")
        print(f"Customer        : {sub['FullName']}")
        print(f"Plan            : {sub['PlanName']}")
        print(f"Speed           : {sub['SpeedMbps']} Mbps")
        print(f"Price           : Rs. {sub['Price']}")
        print(f"Start Date      : {sub['StartDate']}")
        print(f"End Date        : {sub['EndDate']}")
        print(f"Status          : {sub['Status']}")
        print(f"Auto Renew      : {'Yes' if sub['AutoRenew'] else 'No'}")

    def search_subscription(self):

        print("\n===== SEARCH SUBSCRIPTION =====\n")

        subscription_id = int(input("Enter Subscription ID: "))

        sub = self.service.get_subscription_by_id(subscription_id)

        if sub:

            self.print_subscription(sub)

        else:

            print("\nSubscription not found.")

    def pause_subscription(self, subscription_id):

        connection = None
        cursor = None

        try:

            connection = self.get_db_connection()

            cursor = connection.cursor()

            query = """
                UPDATE Subscriptions
                SET Status = 'Paused'
                WHERE SubscriptionID = %s
                AND Status = 'Active'
            """

            cursor.execute(query, (subscription_id,))

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            print(f"Database Error: {e}")
            return False

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    def pause_subscription(self):

        print("\n===== PAUSE SUBSCRIPTION =====\n")

        subscription_id = int(input("Enter Subscription ID: "))

        sub = self.service.get_subscription_by_id(subscription_id)

        if not sub:

            print("\nSubscription not found.")
            return

        self.print_subscription(sub)

        if sub["Status"] != "Active":

            print("\nOnly Active subscriptions can be paused.")
            return

        confirm = input("\nPause this subscription? (Y/N): ").strip().upper()

        if confirm != "Y":

            print("\nOperation cancelled.")
            return

        success = self.service.pause_subscription(subscription_id)

        if success:

            print("\nSubscription paused successfully.")

        else:

            print("\nUnable to pause subscription.")

    
    def resume_subscription(self):

        print("\n===== RESUME SUBSCRIPTION =====\n")

        subscription_id = int(input("Enter Subscription ID: "))

        sub = self.service.get_subscription_by_id(subscription_id)

        if not sub:

            print("\nSubscription not found.")
            return

        self.print_subscription(sub)

        if sub["Status"] != "Paused":

            print("\nOnly Paused subscriptions can be resumed.")
            return

        confirm = input("\nResume this subscription? (Y/N): ").strip().upper()

        if confirm != "Y":

            print("\nOperation cancelled.")
            return

        success = self.service.resume_subscription(subscription_id)

        if success:

            print("\nSubscription resumed successfully.")

        else:

            print("\nUnable to resume subscription.")

        
    def cancel_subscription(self):

        print("\n===== CANCEL SUBSCRIPTION =====\n")

        subscription_id = int(input("Enter Subscription ID: "))

        sub = self.service.get_subscription_by_id(subscription_id)

        if not sub:

            print("\nSubscription not found.")
            return

        self.print_subscription(sub)

        if sub["Status"] not in ("Active", "Paused"):

            print("\nThis subscription cannot be cancelled.")
            return

        confirm = input("\nCancel this subscription? (Y/N): ").strip().upper()

        if confirm != "Y":

            print("\nOperation cancelled.")
            return

        success = self.service.cancel_subscription(subscription_id)

        if success:

            print("\nSubscription cancelled successfully.")

        else:

            print("\nUnable to cancel subscription.")