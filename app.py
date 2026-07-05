from controllers.customer_controller import CustomerController
from controllers.plan_controller import PlanController
from controllers.subscription_controller import SubscriptionController


def main():

    customer_controller = CustomerController()
    plan_controller = PlanController()
    subscription_controller = SubscriptionController()

    while True:

        print("\n" + "=" * 45)
        print("        SubscriberHub v1.0")
        print("=" * 45)
        print("1. Display Customers")
        print("2. Register Customer")
        print("3. Display Plans")
        print("4. Create Subscription")
        print("5. Exit")
        print("=" * 45)

        choice = input("Select an option: ")

        if choice == "1":

            customer_controller.display_customers()

        elif choice == "2":

            customer_controller.register_customer()

        elif choice == "3":

            plan_controller.display_plans()

        elif choice == "4":

            subscription_controller.create_subscription()

        elif choice == "5":

            customer_controller.search_customer()

        elif choice == "6":

            break

        else:

            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()