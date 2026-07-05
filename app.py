from controllers.customer_controller import CustomerController
from controllers.plan_controller import PlanController
from controllers.subscription_controller import SubscriptionController
from controllers.payment_controller import PaymentController
from controllers.ticket_controller import SupportTicketController


def print_main_menu():

    print("\n" + "=" * 50)
    print("             SubscriberHub v1.0")
    print("=" * 50)
    print("1. Customer Management")
    print("2. Plan Management")
    print("3. Subscription Management")
    print("4. Payment Management")
    print("5. Support Ticket Management")
    print("0. Exit")
    print("=" * 50)


def main():

    customer_controller = CustomerController()
    plan_controller = PlanController()
    subscription_controller = SubscriptionController()
    payment_controller = PaymentController()
    ticket_controller = SupportTicketController()

    while True:

        print_main_menu()

        choice = input("Select an option: ").strip()

        if choice == "1":

            customer_controller.customer_menu()

        elif choice == "2":

            plan_controller.plan_menu()

        elif choice == "3":

            subscription_controller.subscription_menu()

        elif choice == "4":

            payment_controller.payment_menu()

        elif choice == "5":

            ticket_controller.ticket_menu()

        elif choice == "0":

            print("\nThank you for using SubscriberHub!")
            break

        else:

            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()